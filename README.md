# Team Neutron Hive - Veritas UConnect
## Team Members:- 
#### 1. Aradhya Pitlawar ([ThunderSmoker](https://github.com/Thundersmoker))
#### 2. Tushar Rathod ([calto16](https://github.com/calto16))
#### 3. Jay Shirgupe ([Jay7221](https://github.com/Jay7221))


# CSI for S3

This project implements a Container Storage Interface ([CSI](https://github.com/container-storage-interface/spec/blob/master/spec.md)) driver for mounting S3 compatible object to Kubernetes pods as a file-system via FUSE.
##### [PPT Link](https://www.canva.com/design/DAF9KNUo4mY/OuM0ppBc16MNESyMq7YuUQ/edit?utm_content=DAF9KNUo4mY&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)



# DEMO VIDEO


[![Demo video](https://img.youtube.com/vi/qZDe0k7s0XQ/0.jpg)](https://www.youtube.com/watch?v=qZDe0k7s0XQ)

##### Click [here](https://www.youtube.com/watch?v=qZDe0k7s0XQ) to watch

## Kubernetes installation

### Requirements

* Kubernetes 1.17+
* Kubernetes has to allow privileged containers
* Docker daemon must allow shared mounts (systemd flag `MountFlags=shared`)
* Running Minio Server [refer this gist](https://gist.github.com/balamurugana/c59e868a36bb8a549fe863d22d6f0678).

## Configuring Docker Daemon for Shared Mounts

To allow shared mounts in the Docker daemon, you can follow these steps:

1. **Locate the Docker systemd unit file:** The Docker systemd unit file is usually located at `/etc/systemd/system/docker.service` or `/lib/systemd/system/docker.service`. Alternatively, you can run "systemctl cat docker.service" to locate file path.

2. **Edit the Docker systemd unit file:** Open the Docker systemd unit file in a text editor with sudo permissions.

3. **Add `MountFlags=shared` option:** Add the `MountFlags=shared` option to the `[Service]` section of the unit file. If the `MountFlags` option already exists, append `shared` to the list of flags.

   ```plaintext
   [Service]
   ...
   MountFlags=shared
   ...

## Reload systemd configuration

After making changes, reload the systemd configuration to apply the changes:

```bash
sudo systemctl daemon-reload
```
## Restart Docker service

Restart the Docker service to apply the new configuration:

```bash
sudo systemctl restart docker
```

### Manual installation

#### 1. Edit your secret with your S3 credentials in deploy/csi-secret.yaml

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: csi-s3-secret
  # Namespace depends on the configuration in the storageclass.yaml
  namespace: kube-system
stringData:
  accessKeyID: <YOUR_ACCESS_KEY_ID>
  secretAccessKey: <YOUR_SECRET_ACCESS_KEY>
  # For AWS set it to "https://s3.<region>.amazonaws.com", for example https://s3.eu-central-1.amazonaws.com
  endpoint: <https://example.net>
  # For AWS set it to AWS region
  #region: ""
```

The region can be empty if you are using some other S3 compatible storage.

Create that secret.yaml above:

```bash
cd deploy/
kubectl create -f csi-secret.yaml
```
#### 2. Deploy the driver

```bash
kubectl create -f provisioner.yaml
kubectl create -f driver.yaml
kubectl create -f csi-s3.yaml
```

#### 3. Create the storage class

```bash
kubectl create -f pod-configuration/storageclass.yaml
```

#### 4. Test the S3 driver

1. Create a pvc using the new storage class:

    ```bash
    kubectl create -f pod-configuration/pvc.yaml
    ```

2. Check if the PVC has been bound:

    ```bash
    $ kubectl get pvc csi-s3-pvc
    NAME         STATUS    VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
    csi-s3-pvc   Bound     pvc-c5d4634f-8507-11e8-9f33-0e243832354b   2Gi        RWO            csi-s3         9s
    ```

### Alternatively , you can run "sudo ./run-csi.sh" in /Execuatbles to automate above complete  process


3. Create a test pod which mounts your volume:

    ```bash
    kubectl create -f pod-configuration/pod.yaml
    ```

    If the pod can start, everything should be working.
  

4. Test the mount

    ```bash
    $ kubectl exec -ti csi-s3-test-nginx bash
    $ mount | grep fuse
    pvc-035763df-0488-4941-9a34-f637292eb95c: on /usr/share/nginx/html/s3 type fuse.geesefs (rw,nosuid,nodev,relatime,user_id=65534,group_id=0,default_permissions,allow_other)
    $ touch /mnt/s3/hello_world
    ```

If something does not work as expected, check the troubleshooting section below.

## Additional configuration

### Bucket

By default, csi-s3 will create a new bucket per volume. The bucket name will match that of the volume ID. If you want your volumes to live in a precreated bucket, you can simply specify the bucket in the storage class parameters:

```yaml
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: csi-s3-existing-bucket
provisioner: ru.yandex.s3.csi
parameters:
  mounter: geesefs
  options: "--memory-limit 1000 --dir-mode 0777 --file-mode 0666"
  bucket: some-existing-bucket-name
```

If the bucket is specified, it will still be created if it does not exist on the backend. Every volume will get its own prefix within the bucket which matches the volume ID. When deleting a volume, also just the prefix will be deleted.


### Mounter

We are using GeeseFS.


#### GeeseFS

* Almost full POSIX compatibility
* Good performance for both small and big files
* Does not store file permissions and custom modification times
* By default runs **outside** of the csi-s3 container using systemd, to not crash
  mountpoints with "Transport endpoint is not connected" when csi-s3 is upgraded
  or restarted. Add `--no-systemd` to `parameters.options` of the `StorageClass`
  to disable this behaviour.


## Troubleshooting

### Issues while creating PVC

Check the logs of the provisioner:

```bash
kubectl logs -l app=csi-provisioner-s3 -c csi-s3
```

### Issues creating containers

1. Ensure feature gate `MountPropagation` is not set to `false`
2. Check the logs of the s3-driver:

```bash
kubectl logs -l app=csi-s3 -c csi-s3
```




