
package driver

import (
	"fmt"
	"os"
	"os/exec"
	"regexp"
	"strconv"

	"github.com/yandex-cloud/k8s-csi-s3/pkg/mounter"
	"github.com/yandex-cloud/k8s-csi-s3/pkg/s3"
	"github.com/golang/glog"
	"golang.org/x/net/context"

	"github.com/container-storage-interface/spec/lib/go/csi"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
	"k8s.io/kubernetes/pkg/util/mount"

	csicommon "github.com/kubernetes-csi/drivers/pkg/csi-common"
)

type nodeServer struct {
	*csicommon.DefaultNodeServer
}

func getMeta(bucketName, prefix string, context map[string]string) *s3.FSMeta {
	mountOptions := make([]string, 0)
	mountOptStr := context[mounter.OptionsKey]
	if mountOptStr != "" {
		re, _ := regexp.Compile(`([^\s"]+|"([^"\\]+|\\")*")+`)
		re2, _ := regexp.Compile(`"([^"\\]+|\\")*"`)
		re3, _ := regexp.Compile(`\\(.)`)
		for _, opt := range re.FindAll([]byte(mountOptStr), -1) {
			opt = re2.ReplaceAllFunc(opt, func(q []byte) []byte {
				return re3.ReplaceAll(q[1 : len(q)-1], []byte("$1"))
			})
			mountOptions = append(mountOptions, string(opt))
		}
	}
	capacity, _ := strconv.ParseInt(context["capacity"], 10, 64)
	return &s3.FSMeta{
		BucketName:    bucketName,
		Prefix:        prefix,
		Mounter:       context[mounter.TypeKey],
		MountOptions:  mountOptions,
		CapacityBytes: capacity,
	}
}

func (ns *nodeServer) NodePublishVolume(ctx context.Context, req *csi.NodePublishVolumeRequest) (*csi.NodePublishVolumeResponse, error) {
	volumeID := req.GetVolumeId()
	targetPath := req.GetTargetPath()
	stagingTargetPath := req.GetStagingTargetPath()

	if req.GetVolumeCapability() == nil {
		return nil, status.Error(codes.InvalidArgument, "Volume capability missing in request")
	}
	if len(volumeID) == 0 {
		return nil, status.Error(codes.InvalidArgument, "Volume ID missing in request")
	}
	if len(stagingTargetPath) == 0 {
		return nil, status.Error(codes.InvalidArgument, "Staging Target path missing in request")
	}
	if len(targetPath) == 0 {
		return nil, status.Error(codes.InvalidArgument, "Target path missing in request")
	}

	notMnt, err := checkMount(stagingTargetPath)
	if err != nil {
		return nil, status.Error(codes.Internal, err.Error())
	}
	if notMnt {
		bucketName, prefix := volumeIDToBucketPrefix(volumeID)
		s3, err := s3.NewClientFromSecret(req.GetSecrets())
		if err != nil {
			return nil, fmt.Errorf("failed to initialize S3 client: %s", err)
		}
		meta := getMeta(bucketName, prefix, req.VolumeContext)
		mounter, err := mounter.New(meta, s3.Config)
		if err != nil {
			return nil, err
		}
		if err := mounter.Mount(stagingTargetPath, volumeID); err != nil {
			return nil, err
		}
	}

	notMnt, err = checkMount(targetPath)
	if err != nil {
		return nil, status.Error(codes.Internal, err.Error())
	}
	if !notMnt {
		return &csi.NodePublishVolumeResponse{}, nil
	}

	readOnly := req.GetReadonly()
	mountFlags := req.GetVolumeCapability().GetMount().GetMountFlags()
	attrib := req.GetVolumeContext()

	glog.V(4).Infof("target %v\nreadonly %v\nvolumeId %v\nattributes %v\nmountflags %v\n",
		targetPath, readOnly, volumeID, attrib, mountFlags)

	cmd := exec.Command("mount", "--bind", stagingTargetPath, targetPath)
	cmd.Stderr = os.Stderr
	glog.V(3).Infof("Binding volume %v from %v to %v", volumeID, stagingTargetPath, targetPath)
	out, err := cmd.Output()
	if err != nil {
		return nil, fmt.Errorf("Error running mount --bind %v %v: %s", stagingTargetPath, targetPath, out)
	}

	glog.V(4).Infof("s3: volume %s successfully mounted to %s", volumeID, targetPath)

	return &csi.NodePublishVolumeResponse{}, nil
}

func (ns *nodeServer) NodeUnpublishVolume(ctx context.Context, req *csi.NodeUnpublishVolumeRequest) (*csi.NodeUnpublishVolumeResponse, error) {
	volumeID := req.GetVolumeId()
	targetPath := req.GetTargetPath()

	if len(volumeID) == 0 {
		return nil, status.Error(codes.InvalidArgument, "Volume ID missing in request")
	}
	if len(targetPath) == 0 {
		return nil, status.Error(codes.InvalidArgument, "Target path missing in request")
	}

	if err := mounter.Unmount(targetPath); err != nil {
		return nil, status.Error(codes.Internal, err.Error())
	}
	glog.V(4).Infof("s3: volume %s has been unmounted.", volumeID)

	return &csi.NodeUnpublishVolumeResponse{}, nil
}

func (ns *nodeServer) NodeStageVolume(ctx context.Context, req *csi.NodeStageVolumeRequest) (*csi.NodeStageVolumeResponse, error) {
	volumeID := req.GetVolumeId()
	stagingTargetPath := req.GetStagingTargetPath()
	bucketName, prefix := volumeIDToBucketPrefix(volumeID)

	if len(volumeID) == 0 {
		return nil, status.Error(codes.InvalidArgument, "Volume ID missing in request")
	}

	if len(stagingTargetPath) == 0 {
		return nil, status.Error(codes.InvalidArgument, "Target path missing in request")
	}

	if req.VolumeCapability == nil {
		return nil, status.Error(codes.InvalidArgument, "NodeStageVolume Volume Capability must be provided")
	}

	notMnt, err := checkMount(stagingTargetPath)
	if err != nil {
		return nil, status.Error(codes.Internal, err.Error())
	}
	if !notMnt {
		return &csi.NodeStageVolumeResponse{}, nil
	}
	client, err := s3.NewClientFromSecret(req.GetSecrets())
	if err != nil {
		return nil, fmt.Errorf("failed to initialize S3 client: %s", err)
	}

	meta := getMeta(bucketName, prefix, req.VolumeContext)
	mounter, err := mounter.New(meta, client.Config)
	if err != nil {
		return nil, err
	}
	if err := mounter.Mount(stagingTargetPath, volumeID); err != nil {
		return nil, err
	}

	return &csi.NodeStageVolumeResponse{}, nil
}

func (ns *nodeServer) NodeUnstageVolume(ctx context.Context, req *csi.NodeUnstageVolumeRequest) (*csi.NodeUnstageVolumeResponse, error) {
	volumeID := req.GetVolumeId()
	stagingTargetPath := req.GetStagingTargetPath()

	if len(volumeID) == 0 {
		return nil, status.Error(codes.InvalidArgument, "Volume ID missing in request")
	}
	if len(stagingTargetPath) == 0 {
		return nil, status.Error(codes.InvalidArgument, "Target path missing in request")
	}

	proc, err := mounter.FindFuseMountProcess(stagingTargetPath)
	if err != nil {
		return nil, err
	}
	exists := false
	if proc == nil {
		exists, err = mounter.SystemdUnmount(volumeID)
		if exists && err != nil {
			return nil, err
		}
	}
	if !exists {
		err = mounter.FuseUnmount(stagingTargetPath)
	}
	glog.V(4).Infof("s3: volume %s has been unmounted from stage path %v.", volumeID, stagingTargetPath)

	return &csi.NodeUnstageVolumeResponse{}, nil
}

func (ns *nodeServer) NodeGetCapabilities(ctx context.Context, req *csi.NodeGetCapabilitiesRequest) (*csi.NodeGetCapabilitiesResponse, error) {
	nscap := &csi.NodeServiceCapability{
		Type: &csi.NodeServiceCapability_Rpc{
			Rpc: &csi.NodeServiceCapability_RPC{
				Type: csi.NodeServiceCapability_RPC_STAGE_UNSTAGE_VOLUME,
			},
		},
	}

	return &csi.NodeGetCapabilitiesResponse{
		Capabilities: []*csi.NodeServiceCapability{
			nscap,
		},
	}, nil
}

func (ns *nodeServer) NodeExpandVolume(ctx context.Context, req *csi.NodeExpandVolumeRequest) (*csi.NodeExpandVolumeResponse, error) {
	return &csi.NodeExpandVolumeResponse{}, status.Error(codes.Unimplemented, "NodeExpandVolume is not implemented")
}

func checkMount(targetPath string) (bool, error) {
	notMnt, err := mount.New("").IsLikelyNotMountPoint(targetPath)
	if err != nil {
		if os.IsNotExist(err) {
			if err = os.MkdirAll(targetPath, 0750); err != nil {
				return false, err
			}
			notMnt = true
		} else {
			return false, err
		}
	}
	return notMnt, nil
}
