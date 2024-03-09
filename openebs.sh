
purva@purva-VirtualBox:~/Desktop$ curl -fsSL https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
Downloading https://get.helm.sh/helm-v3.14.2-linux-amd64.tar.gz
Verifying checksum... Done.
Preparing to install helm into /usr/local/bin
helm installed into /usr/local/bin/helm


purva@purva-VirtualBox:~/Desktop$ helm repo add openebs https://openebs.github.io/charts
"openebs" has been added to your repositories


purva@purva-VirtualBox:~/Desktop$ helm repo update
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "openebs" chart repository
Update Complete. ⎈Happy Helming!⎈


purva@purva-VirtualBox:~/Desktop$ helm install openebs --namespace openebs openebs/openebs --create-namespace
NAME: openebs
LAST DEPLOYED: Sat Mar  9 17:12:52 2024
NAMESPACE: openebs
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
Successfully installed OpenEBS.

Check the status by running: kubectl get pods -n openebs

The default values will install NDM and enable OpenEBS hostpath and device
storage engines along with their default StorageClasses. Use `kubectl get sc`
to see the list of installed OpenEBS StorageClasses.

**Note**: If you are upgrading from the older helm chart that was using cStor
and Jiva (non-csi) volumes, you will have to run the following command to include
the older provisioners:

helm upgrade openebs openebs/openebs \
	--namespace openebs \
	--set legacy.enabled=true \
	--reuse-values

For other engines, you will need to perform a few more additional steps to
enable the engine, configure the engines (e.g. creating pools) and create 
StorageClasses. 

For example, cStor can be enabled using commands like:

helm upgrade openebs openebs/openebs \
	--namespace openebs \
	--set cstor.enabled=true \
	--reuse-values

For more information, 
- view the online documentation at https://openebs.io/docs or
- connect with an active community on Kubernetes slack #openebs channel.


purva@purva-VirtualBox:~/Desktop$ sudo apt-get update
sudo apt-get install -y kubectl
Hit:1 https://download.docker.com/linux/ubuntu focal InRelease
Hit:2 http://in.archive.ubuntu.com/ubuntu jammy InRelease
Get:3 http://in.archive.ubuntu.com/ubuntu jammy-updates InRelease [119 kB]
Get:4 http://security.ubuntu.com/ubuntu jammy-security InRelease [110 kB]
Hit:5 http://in.archive.ubuntu.com/ubuntu jammy-backports InRelease
Fetched 229 kB in 3s (69.3 kB/s)
Reading package lists... Done
W: https://download.docker.com/linux/ubuntu/dists/focal/InRelease: Key is stored in legacy trusted.gpg keyring (/etc/apt/trusted.gpg), see the DEPRECATION section in apt-key(8) for details.
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
E: Unable to locate package kubectl
purva@purva-VirtualBox:~/Desktop$ sudo apt-get update
Hit:1 http://in.archive.ubuntu.com/ubuntu jammy InRelease
Hit:2 https://download.docker.com/linux/ubuntu focal InRelease             
Hit:3 http://in.archive.ubuntu.com/ubuntu jammy-updates InRelease          
Hit:4 http://security.ubuntu.com/ubuntu jammy-security InRelease
Hit:5 http://in.archive.ubuntu.com/ubuntu jammy-backports InRelease
Reading package lists... Done
W: https://download.docker.com/linux/ubuntu/dists/focal/InRelease: Key is stored in legacy trusted.gpg keyring (/etc/apt/trusted.gpg), see the DEPRECATION section in apt-key(8) for details.



purva@purva-VirtualBox:~/Desktop$ curl -sSL https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add 
Warning: apt-key is deprecated. Manage keyring files in trusted.gpg.d instead (see apt-key(8)).
OK


purva@purva-VirtualBox:~/Desktop$  curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   138  100   138    0     0    294      0 --:--:-- --:--:-- --:--:--   295
100 47.4M  100 47.4M    0     0  3529k      0  0:00:13  0:00:13 --:--:-- 3777k


purva@purva-VirtualBox:~/Desktop$ sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl


purva@purva-VirtualBox:~/Desktop$ kubectl version --client
Client Version: v1.29.2
Kustomize Version: v5.0.4-0.20230601165947-6ce0bf390ce3


purva@purva-VirtualBox:~/Desktop$ sudo apt-get install open-iscsi
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  finalrd libisns0 libopeniscsiusr
The following NEW packages will be installed:
  finalrd libisns0 libopeniscsiusr open-iscsi
0 upgraded, 4 newly installed, 0 to remove and 29 not upgraded.
Need to get 494 kB of archives.
After this operation, 1,988 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 libisns0 amd64 0.101-0ubuntu2 [96.3 kB]
Get:2 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 libopeniscsiusr amd64 2.1.5-1ubuntu1 [67.4 kB]
Get:3 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 open-iscsi amd64 2.1.5-1ubuntu1 [323 kB]
Get:4 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 finalrd all 9build1 [7,306 B]                                                                                                                   
Fetched 494 kB in 10s (48.2 kB/s)                                                                                                                                                                          
Preconfiguring packages ...
Selecting previously unselected package libisns0:amd64.
(Reading database ... 202804 files and directories currently installed.)
Preparing to unpack .../libisns0_0.101-0ubuntu2_amd64.deb ...
Unpacking libisns0:amd64 (0.101-0ubuntu2) ...
Selecting previously unselected package libopeniscsiusr.
Preparing to unpack .../libopeniscsiusr_2.1.5-1ubuntu1_amd64.deb ...
Unpacking libopeniscsiusr (2.1.5-1ubuntu1) ...
Selecting previously unselected package open-iscsi.
Preparing to unpack .../open-iscsi_2.1.5-1ubuntu1_amd64.deb ...
Unpacking open-iscsi (2.1.5-1ubuntu1) ...
Selecting previously unselected package finalrd.
Preparing to unpack .../finalrd_9build1_all.deb ...
Unpacking finalrd (9build1) ...
Setting up finalrd (9build1) ...
Created symlink /etc/systemd/system/sysinit.target.wants/finalrd.service → /lib/systemd/system/finalrd.service.
Setting up libopeniscsiusr (2.1.5-1ubuntu1) ...
Setting up libisns0:amd64 (0.101-0ubuntu2) ...
Setting up open-iscsi (2.1.5-1ubuntu1) ...
iscsid.service is a disabled or a static unit, not starting it.
Created symlink /etc/systemd/system/sockets.target.wants/iscsid.socket → /lib/systemd/system/iscsid.socket.
Created symlink /etc/systemd/system/iscsi.service → /lib/systemd/system/open-iscsi.service.
Created symlink /etc/systemd/system/sysinit.target.wants/open-iscsi.service → /lib/systemd/system/open-iscsi.service.
Processing triggers for libc-bin (2.35-0ubuntu3.6) ...
Processing triggers for man-db (2.10.2-1) ...
Processing triggers for initramfs-tools (0.140ubuntu13.4) ...
update-initramfs: Generating /boot/initrd.img-6.5.0-25-generic


purva@purva-VirtualBox:~/Desktop$ sudo systemctl status iscsid.service
○ iscsid.service - iSCSI initiator daemon (iscsid)
     Loaded: loaded (/lib/systemd/system/iscsid.service; disabled; vendor preset: enabled)
     Active: inactive (dead)
TriggeredBy: ● iscsid.socket
       Docs: man:iscsid(8)
purva@purva-VirtualBox:~/Desktop$ sudo systemctl start iscsid.service
purva@purva-VirtualBox:~/Desktop$ sudo systemctl status iscsid.service
● iscsid.service - iSCSI initiator daemon (iscsid)
     Loaded: loaded (/lib/systemd/system/iscsid.service; disabled; vendor preset: enabled)
     Active: active (running) since Sat 2024-03-09 17:32:45 IST; 4s ago
TriggeredBy: ● iscsid.socket
       Docs: man:iscsid(8)
    Process: 60994 ExecStartPre=/lib/open-iscsi/startup-checks.sh (code=exited, status=0/SUCCESS)
    Process: 61197 ExecStart=/sbin/iscsid (code=exited, status=0/SUCCESS)
   Main PID: 61199 (iscsid)
      Tasks: 2 (limit: 5800)
     Memory: 2.8M
        CPU: 15ms
     CGroup: /system.slice/iscsid.service
             ├─61198 /sbin/iscsid
             └─61199 /sbin/iscsid

Mar 09 17:32:34 purva-VirtualBox systemd[1]: Starting iSCSI initiator daemon (iscsid)...
Mar 09 17:32:45 purva-VirtualBox iscsid[61197]: iSCSI logger with pid=61198 started!
Mar 09 17:32:45 purva-VirtualBox systemd[1]: Started iSCSI initiator daemon (iscsid).
Mar 09 17:32:46 purva-VirtualBox iscsid[61198]: iSCSI daemon with pid=61199 started!

purva@purva-VirtualBox:~/Desktop$ sudo systemctl enable --now iscsid
Synchronizing state of iscsid.service with SysV service script with /lib/systemd/systemd-sysv-install.
Executing: /lib/systemd/systemd-sysv-install enable iscsid
Created symlink /etc/systemd/system/sysinit.target.wants/iscsid.service → /lib/systemd/system/iscsid.service.


purva@purva-VirtualBox:~/Desktop$ systemctl status iscsid
● iscsid.service - iSCSI initiator daemon (iscsid)
     Loaded: loaded (/lib/systemd/system/iscsid.service; enabled; vendor preset: enabled)
     Active: active (running) since Sat 2024-03-09 17:32:45 IST; 1min 7s ago
TriggeredBy: ● iscsid.socket
       Docs: man:iscsid(8)
   Main PID: 61199 (iscsid)
      Tasks: 2 (limit: 5800)
     Memory: 2.8M
        CPU: 17ms
     CGroup: /system.slice/iscsid.service
             ├─61198 /sbin/iscsid
             └─61199 /sbin/iscsid

Mar 09 17:32:34 purva-VirtualBox systemd[1]: Starting iSCSI initiator daemon (iscsid)...
Mar 09 17:32:45 purva-VirtualBox iscsid[61197]: iSCSI logger with pid=61198 started!
Mar 09 17:32:45 purva-VirtualBox systemd[1]: Started iSCSI initiator daemon (iscsid).
Mar 09 17:32:46 purva-VirtualBox iscsid[61198]: iSCSI daemon with pid=61199 started!


purva@purva-VirtualBox:~/Desktop$ sudo apt-get update
Hit:1 https://download.docker.com/linux/ubuntu focal InRelease
Hit:2 http://security.ubuntu.com/ubuntu jammy-security InRelease
Hit:3 http://in.archive.ubuntu.com/ubuntu jammy InRelease
Hit:4 http://in.archive.ubuntu.com/ubuntu jammy-updates InRelease
Hit:5 http://in.archive.ubuntu.com/ubuntu jammy-backports InRelease
Reading package lists... Done
W: https://download.docker.com/linux/ubuntu/dists/focal/InRelease: Key is stored in legacy trusted.gpg keyring (/etc/apt/trusted.gpg), see the DEPRECATION section in apt-key(8) for details.


purva@purva-VirtualBox:~/Desktop$ kubectl config set-context csi_context --cluster=c1 --user=shrinirva --namespace=open_ebs
Context "csi_context" created.


purva@purva-VirtualBox:~/Desktop$ kubectl config use-context csi_context
Switched to context "csi_context".

purva@purva-VirtualBox:~/Desktop$ minikube start
😄  minikube v1.32.0 on Ubuntu 22.04 (vbox/amd64)
✨  Using the docker driver based on existing profile
👍  Starting control plane node minikube in cluster minikube
🚜  Pulling base image ...
🏃  Updating the running docker "minikube" container ...
🐳  Preparing Kubernetes v1.28.3 on Docker 24.0.7 ...
🔎  Verifying Kubernetes components...
    ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
🌟  Enabled addons: storage-provisioner, default-storageclass
🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default

purva@purva-VirtualBox:~/Desktop$ minikube status
minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured

purva@purva-VirtualBox:~/Desktop$ helm repo add openebs https://openebs.github.io/charts
"openebs" already exists with the same configuration, skipping

purva@purva-VirtualBox:~/Desktop$ helm repo update
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "openebs" chart repository
Update Complete. ⎈Happy Helming!⎈



purva@purva-VirtualBox:~/Desktop$ helm ls -n openebs
NAME   	NAMESPACE	REVISION	UPDATED                                	STATUS  	CHART         	APP VERSION
openebs	openebs  	1       	2024-03-09 17:12:52.496835282 +0530 IST	deployed	openebs-3.10.0	3.10.0     

purva@purva-VirtualBox:~/Desktop$ kubectl apply -f https://openebs.github.io/charts/openebs-operator.yaml
namespace/openebs unchanged
serviceaccount/openebs-maya-operator unchanged
clusterrole.rbac.authorization.k8s.io/openebs-maya-operator unchanged
clusterrolebinding.rbac.authorization.k8s.io/openebs-maya-operator unchanged
customresourcedefinition.apiextensions.k8s.io/blockdevices.openebs.io configured
customresourcedefinition.apiextensions.k8s.io/blockdeviceclaims.openebs.io configured
configmap/openebs-ndm-config unchanged
Warning: resource daemonsets/openebs-ndm is missing the kubectl.kubernetes.io/last-applied-configuration annotation which is required by kubectl apply. kubectl apply should only be used on resources created declaratively by either kubectl create --save-config or kubectl apply. The missing annotation will be patched automatically.
Warning: resource deployments/openebs-ndm-operator is missing the kubectl.kubernetes.io/last-applied-configuration annotation which is required by kubectl apply. kubectl apply should only be used on resources created declaratively by either kubectl create --save-config or kubectl apply. The missing annotation will be patched automatically.
deployment.apps/openebs-ndm-cluster-exporter configured
service/openebs-ndm-cluster-exporter-service unchanged
daemonset.apps/openebs-ndm-node-exporter configured
service/openebs-ndm-node-exporter-service unchanged
Warning: resource deployments/openebs-localpv-provisioner is missing the kubectl.kubernetes.io/last-applied-configuration annotation which is required by kubectl apply. kubectl apply should only be used on resources created declaratively by either kubectl create --save-config or kubectl apply. The missing annotation will be patched automatically.
storageclass.storage.k8s.io/openebs-hostpath unchanged
storageclass.storage.k8s.io/openebs-device unchanged
Error from server (Invalid): error when applying patch:
{"metadata":{"annotations":{"kubectl.kubernetes.io/last-applied-configuration":"{\"apiVersion\":\"apps/v1\",\"kind\":\"DaemonSet\",\"metadata\":{\"annotations\":{},\"labels\":{\"name\":\"openebs-ndm\",\"openebs.io/component-name\":\"ndm\",\"openebs.io/version\":\"3.5.0\"},\"name\":\"openebs-ndm\",\"namespace\":\"openebs\"},\"spec\":{\"selector\":{\"matchLabels\":{\"name\":\"openebs-ndm\",\"openebs.io/component-name\":\"ndm\"}},\"template\":{\"metadata\":{\"labels\":{\"name\":\"openebs-ndm\",\"openebs.io/component-name\":\"ndm\",\"openebs.io/version\":\"3.5.0\"}},\"spec\":{\"containers\":[{\"args\":[\"-v=4\",\"--feature-gates=\\\"GPTBasedUUID\\\"\"],\"env\":[{\"name\":\"NAMESPACE\",\"valueFrom\":{\"fieldRef\":{\"fieldPath\":\"metadata.namespace\"}}},{\"name\":\"NODE_NAME\",\"valueFrom\":{\"fieldRef\":{\"fieldPath\":\"spec.nodeName\"}}},{\"name\":\"SPARSE_FILE_DIR\",\"value\":\"/var/openebs/sparse\"},{\"name\":\"SPARSE_FILE_SIZE\",\"value\":\"10737418240\"},{\"name\":\"SPARSE_FILE_COUNT\",\"value\":\"0\"}],\"image\":\"openebs/node-disk-manager:2.1.0\",\"imagePullPolicy\":\"IfNotPresent\",\"livenessProbe\":{\"exec\":{\"command\":[\"pgrep\",\"ndm\"]},\"initialDelaySeconds\":30,\"periodSeconds\":60},\"name\":\"node-disk-manager\",\"securityContext\":{\"privileged\":true},\"volumeMounts\":[{\"mountPath\":\"/host/node-disk-manager.config\",\"name\":\"config\",\"readOnly\":true,\"subPath\":\"node-disk-manager.config\"},{\"mountPath\":\"/run/udev\",\"name\":\"udev\"},{\"mountPath\":\"/host/proc\",\"name\":\"procmount\",\"readOnly\":true},{\"mountPath\":\"/dev\",\"name\":\"devmount\"},{\"mountPath\":\"/var/openebs/ndm\",\"name\":\"basepath\"},{\"mountPath\":\"/var/openebs/sparse\",\"name\":\"sparsepath\"}]}],\"hostNetwork\":true,\"serviceAccountName\":\"openebs-maya-operator\",\"volumes\":[{\"configMap\":{\"name\":\"openebs-ndm-config\"},\"name\":\"config\"},{\"hostPath\":{\"path\":\"/run/udev\",\"type\":\"Directory\"},\"name\":\"udev\"},{\"hostPath\":{\"path\":\"/proc\",\"type\":\"Directory\"},\"name\":\"procmount\"},{\"hostPath\":{\"path\":\"/dev\",\"type\":\"Directory\"},\"name\":\"devmount\"},{\"hostPath\":{\"path\":\"/var/openebs/ndm\",\"type\":\"DirectoryOrCreate\"},\"name\":\"basepath\"},{\"hostPath\":{\"path\":\"/var/openebs/sparse\"},\"name\":\"sparsepath\"}]}},\"updateStrategy\":{\"type\":\"RollingUpdate\"}}}\n"},"labels":{"name":"openebs-ndm","openebs.io/version":"3.5.0"}},"spec":{"selector":{"matchLabels":{"name":"openebs-ndm","openebs.io/component-name":"ndm"}},"template":{"metadata":{"labels":{"openebs.io/version":"3.5.0"}},"spec":{"$setElementOrder/containers":[{"name":"node-disk-manager"}],"containers":[{"args":["-v=4","--feature-gates=\"GPTBasedUUID\""],"env":[{"name":"NAMESPACE","valueFrom":{"fieldRef":{"fieldPath":"metadata.namespace"}}},{"name":"NODE_NAME","valueFrom":{"fieldRef":{"fieldPath":"spec.nodeName"}}},{"name":"SPARSE_FILE_DIR","value":"/var/openebs/sparse"},{"name":"SPARSE_FILE_SIZE","value":"10737418240"},{"name":"SPARSE_FILE_COUNT","value":"0"}],"image":"openebs/node-disk-manager:2.1.0","imagePullPolicy":"IfNotPresent","livenessProbe":{"exec":{"command":["pgrep","ndm"]},"initialDelaySeconds":30,"periodSeconds":60},"name":"node-disk-manager","securityContext":{"privileged":true},"volumeMounts":[{"mountPath":"/host/node-disk-manager.config","name":"config","readOnly":true,"subPath":"node-disk-manager.config"},{"mountPath":"/run/udev","name":"udev"},{"mountPath":"/host/proc","name":"procmount","readOnly":true},{"mountPath":"/dev","name":"devmount"},{"mountPath":"/var/openebs/ndm","name":"basepath"},{"mountPath":"/var/openebs/sparse","name":"sparsepath"}]}],"serviceAccountName":"openebs-maya-operator"}}}}
to:
Resource: "apps/v1, Resource=daemonsets", GroupVersionKind: "apps/v1, Kind=DaemonSet"
Name: "openebs-ndm", Namespace: "openebs"
for: "https://openebs.github.io/charts/openebs-operator.yaml": error when patching "https://openebs.github.io/charts/openebs-operator.yaml": DaemonSet.apps "openebs-ndm" is invalid: spec.selector: Invalid value: v1.LabelSelector{MatchLabels:map[string]string{"app":"openebs", "component":"ndm", "name":"openebs-ndm", "openebs.io/component-name":"ndm", "release":"openebs"}, MatchExpressions:[]v1.LabelSelectorRequirement(nil)}: field is immutable
Error from server (Invalid): error when applying patch:
{"metadata":{"annotations":{"kubectl.kubernetes.io/last-applied-configuration":"{\"apiVersion\":\"apps/v1\",\"kind\":\"Deployment\",\"metadata\":{\"annotations\":{},\"labels\":{\"name\":\"openebs-ndm-operator\",\"openebs.io/component-name\":\"ndm-operator\",\"openebs.io/version\":\"3.5.0\"},\"name\":\"openebs-ndm-operator\",\"namespace\":\"openebs\"},\"spec\":{\"replicas\":1,\"selector\":{\"matchLabels\":{\"name\":\"openebs-ndm-operator\",\"openebs.io/component-name\":\"ndm-operator\"}},\"strategy\":{\"type\":\"Recreate\"},\"template\":{\"metadata\":{\"labels\":{\"name\":\"openebs-ndm-operator\",\"openebs.io/component-name\":\"ndm-operator\",\"openebs.io/version\":\"3.5.0\"}},\"spec\":{\"containers\":[{\"env\":[{\"name\":\"WATCH_NAMESPACE\",\"valueFrom\":{\"fieldRef\":{\"fieldPath\":\"metadata.namespace\"}}},{\"name\":\"POD_NAME\",\"valueFrom\":{\"fieldRef\":{\"fieldPath\":\"metadata.name\"}}},{\"name\":\"SERVICE_ACCOUNT\",\"valueFrom\":{\"fieldRef\":{\"fieldPath\":\"spec.serviceAccountName\"}}},{\"name\":\"OPERATOR_NAME\",\"value\":\"node-disk-operator\"},{\"name\":\"CLEANUP_JOB_IMAGE\",\"value\":\"openebs/linux-utils:3.5.0\"}],\"image\":\"openebs/node-disk-operator:2.1.0\",\"imagePullPolicy\":\"IfNotPresent\",\"livenessProbe\":{\"httpGet\":{\"path\":\"/healthz\",\"port\":8585},\"initialDelaySeconds\":15,\"periodSeconds\":20},\"name\":\"node-disk-operator\",\"readinessProbe\":{\"httpGet\":{\"path\":\"/readyz\",\"port\":8585},\"initialDelaySeconds\":5,\"periodSeconds\":10}}],\"serviceAccountName\":\"openebs-maya-operator\"}}}}\n"},"labels":{"name":"openebs-ndm-operator","openebs.io/version":"3.5.0"}},"spec":{"selector":{"matchLabels":{"name":"openebs-ndm-operator","openebs.io/component-name":"ndm-operator"}},"template":{"metadata":{"labels":{"name":"openebs-ndm-operator","openebs.io/version":"3.5.0"}},"spec":{"$setElementOrder/containers":[{"name":"node-disk-operator"}],"containers":[{"env":[{"name":"WATCH_NAMESPACE","valueFrom":{"fieldRef":{"fieldPath":"metadata.namespace"}}},{"name":"POD_NAME","valueFrom":{"fieldRef":{"fieldPath":"metadata.name"}}},{"name":"SERVICE_ACCOUNT","valueFrom":{"fieldRef":{"fieldPath":"spec.serviceAccountName"}}},{"name":"OPERATOR_NAME","value":"node-disk-operator"},{"name":"CLEANUP_JOB_IMAGE","value":"openebs/linux-utils:3.5.0"}],"image":"openebs/node-disk-operator:2.1.0","imagePullPolicy":"IfNotPresent","livenessProbe":{"httpGet":{"path":"/healthz","port":8585},"initialDelaySeconds":15,"periodSeconds":20},"name":"node-disk-operator","readinessProbe":{"httpGet":{"path":"/readyz","port":8585},"initialDelaySeconds":5,"periodSeconds":10}}],"serviceAccountName":"openebs-maya-operator"}}}}
to:
Resource: "apps/v1, Resource=deployments", GroupVersionKind: "apps/v1, Kind=Deployment"
Name: "openebs-ndm-operator", Namespace: "openebs"
for: "https://openebs.github.io/charts/openebs-operator.yaml": error when patching "https://openebs.github.io/charts/openebs-operator.yaml": Deployment.apps "openebs-ndm-operator" is invalid: spec.selector: Invalid value: v1.LabelSelector{MatchLabels:map[string]string{"app":"openebs", "name":"openebs-ndm-operator", "openebs.io/component-name":"ndm-operator", "release":"openebs"}, MatchExpressions:[]v1.LabelSelectorRequirement(nil)}: field is immutable
Error from server (Invalid): error when applying patch:
{"metadata":{"annotations":{"kubectl.kubernetes.io/last-applied-configuration":"{\"apiVersion\":\"apps/v1\",\"kind\":\"Deployment\",\"metadata\":{\"annotations\":{},\"labels\":{\"name\":\"openebs-localpv-provisioner\",\"openebs.io/component-name\":\"openebs-localpv-provisioner\",\"openebs.io/version\":\"3.5.0\"},\"name\":\"openebs-localpv-provisioner\",\"namespace\":\"openebs\"},\"spec\":{\"replicas\":1,\"selector\":{\"matchLabels\":{\"name\":\"openebs-localpv-provisioner\",\"openebs.io/component-name\":\"openebs-localpv-provisioner\"}},\"strategy\":{\"type\":\"Recreate\"},\"template\":{\"metadata\":{\"labels\":{\"name\":\"openebs-localpv-provisioner\",\"openebs.io/component-name\":\"openebs-localpv-provisioner\",\"openebs.io/version\":\"3.5.0\"}},\"spec\":{\"containers\":[{\"args\":[\"--bd-time-out=$(BDC_BD_BIND_RETRIES)\"],\"env\":[{\"name\":\"BDC_BD_BIND_RETRIES\",\"value\":\"12\"},{\"name\":\"NODE_NAME\",\"valueFrom\":{\"fieldRef\":{\"fieldPath\":\"spec.nodeName\"}}},{\"name\":\"OPENEBS_NAMESPACE\",\"valueFrom\":{\"fieldRef\":{\"fieldPath\":\"metadata.namespace\"}}},{\"name\":\"OPENEBS_SERVICE_ACCOUNT\",\"valueFrom\":{\"fieldRef\":{\"fieldPath\":\"spec.serviceAccountName\"}}},{\"name\":\"OPENEBS_IO_ENABLE_ANALYTICS\",\"value\":\"true\"},{\"name\":\"OPENEBS_IO_INSTALLER_TYPE\",\"value\":\"openebs-operator\"},{\"name\":\"OPENEBS_IO_HELPER_IMAGE\",\"value\":\"openebs/linux-utils:3.5.0\"},{\"name\":\"OPENEBS_IO_BASE_PATH\",\"value\":\"/var/openebs/local\"}],\"image\":\"openebs/provisioner-localpv:3.4.0\",\"imagePullPolicy\":\"IfNotPresent\",\"livenessProbe\":{\"exec\":{\"command\":[\"sh\",\"-c\",\"test `pgrep -c \\\"^provisioner-loc.*\\\"` = 1\"]},\"initialDelaySeconds\":30,\"periodSeconds\":60},\"name\":\"openebs-provisioner-hostpath\"}],\"serviceAccountName\":\"openebs-maya-operator\"}}}}\n"},"labels":{"name":"openebs-localpv-provisioner","openebs.io/version":"3.5.0"}},"spec":{"selector":{"matchLabels":{"name":"openebs-localpv-provisioner","openebs.io/component-name":"openebs-localpv-provisioner"}},"template":{"metadata":{"labels":{"openebs.io/version":"3.5.0"}},"spec":{"$setElementOrder/containers":[{"name":"openebs-provisioner-hostpath"}],"containers":[{"args":["--bd-time-out=$(BDC_BD_BIND_RETRIES)"],"env":[{"name":"BDC_BD_BIND_RETRIES","value":"12"},{"name":"NODE_NAME","valueFrom":{"fieldRef":{"fieldPath":"spec.nodeName"}}},{"name":"OPENEBS_NAMESPACE","valueFrom":{"fieldRef":{"fieldPath":"metadata.namespace"}}},{"name":"OPENEBS_SERVICE_ACCOUNT","valueFrom":{"fieldRef":{"fieldPath":"spec.serviceAccountName"}}},{"name":"OPENEBS_IO_ENABLE_ANALYTICS","value":"true"},{"name":"OPENEBS_IO_INSTALLER_TYPE","value":"openebs-operator"},{"name":"OPENEBS_IO_HELPER_IMAGE","value":"openebs/linux-utils:3.5.0"},{"name":"OPENEBS_IO_BASE_PATH","value":"/var/openebs/local"}],"image":"openebs/provisioner-localpv:3.4.0","imagePullPolicy":"IfNotPresent","livenessProbe":{"exec":{"command":["sh","-c","test `pgrep -c \"^provisioner-loc.*\"` = 1"]},"initialDelaySeconds":30,"periodSeconds":60},"name":"openebs-provisioner-hostpath"}],"serviceAccountName":"openebs-maya-operator"}}}}
to:
Resource: "apps/v1, Resource=deployments", GroupVersionKind: "apps/v1, Kind=Deployment"
Name: "openebs-localpv-provisioner", Namespace: "openebs"
for: "https://openebs.github.io/charts/openebs-operator.yaml": error when patching "https://openebs.github.io/charts/openebs-operator.yaml": Deployment.apps "openebs-localpv-provisioner" is invalid: spec.selector: Invalid value: v1.LabelSelector{MatchLabels:map[string]string{"app":"openebs", "name":"openebs-localpv-provisioner", "openebs.io/component-name":"openebs-localpv-provisioner", "release":"openebs"}, MatchExpressions:[]v1.LabelSelectorRequirement(nil)}: field is immutable
purva@purva-VirtualBox:~/Desktop$ ls
kubectl  minikube-linux-amd64
purva@purva-VirtualBox:~/Desktop$ ls
kubectl  minikube-linux-amd64  openebs-operator.yaml
purva@purva-VirtualBox:~/Desktop$ kubectl apply -f openebs-operator.yaml
namespace/openebs unchanged
serviceaccount/openebs-maya-operator unchanged
clusterrole.rbac.authorization.k8s.io/openebs-maya-operator unchanged
clusterrolebinding.rbac.authorization.k8s.io/openebs-maya-operator unchanged
customresourcedefinition.apiextensions.k8s.io/blockdevices.openebs.io configured
customresourcedefinition.apiextensions.k8s.io/blockdeviceclaims.openebs.io configured
configmap/openebs-ndm-config unchanged
Warning: resource daemonsets/openebs-ndm is missing the kubectl.kubernetes.io/last-applied-configuration annotation which is required by kubectl apply. kubectl apply should only be used on resources created declaratively by either kubectl create --save-config or kubectl apply. The missing annotation will be patched automatically.
Warning: resource deployments/openebs-ndm-operator is missing the kubectl.kubernetes.io/last-applied-configuration annotation which is required by kubectl apply. kubectl apply should only be used on resources created declaratively by either kubectl create --save-config or kubectl apply. The missing annotation will be patched automatically.
deployment.apps/openebs-ndm-cluster-exporter unchanged
service/openebs-ndm-cluster-exporter-service unchanged
daemonset.apps/openebs-ndm-node-exporter unchanged
service/openebs-ndm-node-exporter-service unchanged
Warning: resource deployments/openebs-localpv-provisioner is missing the kubectl.kubernetes.io/last-applied-configuration annotation which is required by kubectl apply. kubectl apply should only be used on resources created declaratively by either kubectl create --save-config or kubectl apply. The missing annotation will be patched automatically.
storageclass.storage.k8s.io/openebs-hostpath unchanged
storageclass.storage.k8s.io/openebs-device unchanged
Error from server (Invalid): error when applying patch:
{"metadata":{"annotations":{"kubectl.kubernetes.io/last-applied-configuration":"{\"apiVersion\":\"apps/v1\",\"kind\":\"DaemonSet\",\"metadata\":{\"annotations\":{},\"labels\":{\"name\":\"openebs-ndm\",\"openebs.io/component-name\":\"ndm\",\"openebs.io/version\":\"3.5.0\"},\"name\":\"openebs-ndm\",\"namespace\":\"openebs\"},\"spec\":{\"selector\":{\"matchLabels\":{\"name\":\"openebs-ndm\",\"openebs.io/component-name\":\"ndm\"}},\"template\":{\"metadata\":{\"labels\":{\"name\":\"openebs-ndm\",\"openebs.io/component-name\":\"ndm\",\"openebs.io/version\":\"3.5.0\"}},\"spec\":{\"containers\":[{\"args\":[\"-v=4\",\"--feature-gates=\\\"GPTBasedUUID\\\"\"],\"env\":[{\"name\":\"NAMESPACE\",\"valueFrom\":{\"fieldRef\":{\"fieldPath\":\"metadata.namespace\"}}},{\"name\":\"NODE_NAME\",\"valueFrom\":{\"fieldRef\":{\"fieldPath\":\"spec.nodeName\"}}},{\"name\":\"SPARSE_FILE_DIR\",\"value\":\"/var/openebs/sparse\"},{\"name\":\"SPARSE_FILE_SIZE\",\"value\":\"10737418240\"},{\"name\":\"SPARSE_FILE_COUNT\",\"value\":\"0\"}],\"image\":\"openebs/node-disk-manager:2.1.0\",\"imagePullPolicy\":\"IfNotPresent\",\"livenessProbe\":{\"exec\":{\"command\":[\"pgrep\",\"ndm\"]},\"initialDelaySeconds\":30,\"periodSeconds\":60},\"name\":\"node-disk-manager\",\"securityContext\":{\"privileged\":true},\"volumeMounts\":[{\"mountPath\":\"/host/node-disk-manager.config\",\"name\":\"config\",\"readOnly\":true,\"subPath\":\"node-disk-manager.config\"},{\"mountPath\":\"/run/udev\",\"name\":\"udev\"},{\"mountPath\":\"/host/proc\",\"name\":\"procmount\",\"readOnly\":true},{\"mountPath\":\"/dev\",\"name\":\"devmount\"},{\"mountPath\":\"/var/openebs/ndm\",\"name\":\"basepath\"},{\"mountPath\":\"/var/openebs/sparse\",\"name\":\"sparsepath\"}]}],\"hostNetwork\":true,\"serviceAccountName\":\"openebs-maya-operator\",\"volumes\":[{\"configMap\":{\"name\":\"openebs-ndm-config\"},\"name\":\"config\"},{\"hostPath\":{\"path\":\"/run/udev\",\"type\":\"Directory\"},\"name\":\"udev\"},{\"hostPath\":{\"path\":\"/proc\",\"type\":\"Directory\"},\"name\":\"procmount\"},{\"hostPath\":{\"path\":\"/dev\",\"type\":\"Directory\"},\"name\":\"devmount\"},{\"hostPath\":{\"path\":\"/var/openebs/ndm\",\"type\":\"DirectoryOrCreate\"},\"name\":\"basepath\"},{\"hostPath\":{\"path\":\"/var/openebs/sparse\"},\"name\":\"sparsepath\"}]}},\"updateStrategy\":{\"type\":\"RollingUpdate\"}}}\n"},"labels":{"name":"openebs-ndm","openebs.io/version":"3.5.0"}},"spec":{"selector":{"matchLabels":{"name":"openebs-ndm","openebs.io/component-name":"ndm"}},"template":{"metadata":{"labels":{"openebs.io/version":"3.5.0"}},"spec":{"$setElementOrder/containers":[{"name":"node-disk-manager"}],"containers":[{"args":["-v=4","--feature-gates=\"GPTBasedUUID\""],"env":[{"name":"NAMESPACE","valueFrom":{"fieldRef":{"fieldPath":"metadata.namespace"}}},{"name":"NODE_NAME","valueFrom":{"fieldRef":{"fieldPath":"spec.nodeName"}}},{"name":"SPARSE_FILE_DIR","value":"/var/openebs/sparse"},{"name":"SPARSE_FILE_SIZE","value":"10737418240"},{"name":"SPARSE_FILE_COUNT","value":"0"}],"image":"openebs/node-disk-manager:2.1.0","imagePullPolicy":"IfNotPresent","livenessProbe":{"exec":{"command":["pgrep","ndm"]},"initialDelaySeconds":30,"periodSeconds":60},"name":"node-disk-manager","securityContext":{"privileged":true},"volumeMounts":[{"mountPath":"/host/node-disk-manager.config","name":"config","readOnly":true,"subPath":"node-disk-manager.config"},{"mountPath":"/run/udev","name":"udev"},{"mountPath":"/host/proc","name":"procmount","readOnly":true},{"mountPath":"/dev","name":"devmount"},{"mountPath":"/var/openebs/ndm","name":"basepath"},{"mountPath":"/var/openebs/sparse","name":"sparsepath"}]}],"serviceAccountName":"openebs-maya-operator"}}}}
to:
Resource: "apps/v1, Resource=daemonsets", GroupVersionKind: "apps/v1, Kind=DaemonSet"
Name: "openebs-ndm", Namespace: "openebs"
for: "openebs-operator.yaml": error when patching "openebs-operator.yaml": DaemonSet.apps "openebs-ndm" is invalid: spec.selector: Invalid value: v1.LabelSelector{MatchLabels:map[string]string{"app":"openebs", "component":"ndm", "name":"openebs-ndm", "openebs.io/component-name":"ndm", "release":"openebs"}, MatchExpressions:[]v1.LabelSelectorRequirement(nil)}: field is immutable
Error from server (Invalid): error when applying patch:
{"metadata":{"annotations":{"kubectl.kubernetes.io/last-applied-configuration":"{\"apiVersion\":\"apps/v1\",\"kind\":\"Deployment\",\"metadata\":{\"annotations\":{},\"labels\":{\"name\":\"openebs-ndm-operator\",\"openebs.io/component-name\":\"ndm-operator\",\"openebs.io/version\":\"3.5.0\"},\"name\":\"openebs-ndm-operator\",\"namespace\":\"openebs\"},\"spec\":{\"replicas\":1,\"selector\":{\"matchLabels\":{\"name\":\"openebs-ndm-operator\",\"openebs.io/component-name\":\"ndm-operator\"}},\"strategy\":{\"type\":\"Recreate\"},\"template\":{\"metadata\":{\"labels\":{\"name\":\"openebs-ndm-operator\",\"openebs.io/component-name\":\"ndm-operator\",\"openebs.io/version\":\"3.5.0\"}},\"spec\":{\"containers\":[{\"env\":[{\"name\":\"WATCH_NAMESPACE\",\"valueFrom\":{\"fieldRef\":{\"fieldPath\":\"metadata.namespace\"}}},{\"name\":\"POD_NAME\",\"valueFrom\":{\"fieldRef\":{\"fieldPath\":\"metadata.name\"}}},{\"name\":\"SERVICE_ACCOUNT\",\"valueFrom\":{\"fieldRef\":{\"fieldPath\":\"spec.serviceAccountName\"}}},{\"name\":\"OPERATOR_NAME\",\"value\":\"node-disk-operator\"},{\"name\":\"CLEANUP_JOB_IMAGE\",\"value\":\"openebs/linux-utils:3.5.0\"}],\"image\":\"openebs/node-disk-operator:2.1.0\",\"imagePullPolicy\":\"IfNotPresent\",\"livenessProbe\":{\"httpGet\":{\"path\":\"/healthz\",\"port\":8585},\"initialDelaySeconds\":15,\"periodSeconds\":20},\"name\":\"node-disk-operator\",\"readinessProbe\":{\"httpGet\":{\"path\":\"/readyz\",\"port\":8585},\"initialDelaySeconds\":5,\"periodSeconds\":10}}],\"serviceAccountName\":\"openebs-maya-operator\"}}}}\n"},"labels":{"name":"openebs-ndm-operator","openebs.io/version":"3.5.0"}},"spec":{"selector":{"matchLabels":{"name":"openebs-ndm-operator","openebs.io/component-name":"ndm-operator"}},"template":{"metadata":{"labels":{"name":"openebs-ndm-operator","openebs.io/version":"3.5.0"}},"spec":{"$setElementOrder/containers":[{"name":"node-disk-operator"}],"containers":[{"env":[{"name":"WATCH_NAMESPACE","valueFrom":{"fieldRef":{"fieldPath":"metadata.namespace"}}},{"name":"POD_NAME","valueFrom":{"fieldRef":{"fieldPath":"metadata.name"}}},{"name":"SERVICE_ACCOUNT","valueFrom":{"fieldRef":{"fieldPath":"spec.serviceAccountName"}}},{"name":"OPERATOR_NAME","value":"node-disk-operator"},{"name":"CLEANUP_JOB_IMAGE","value":"openebs/linux-utils:3.5.0"}],"image":"openebs/node-disk-operator:2.1.0","imagePullPolicy":"IfNotPresent","livenessProbe":{"httpGet":{"path":"/healthz","port":8585},"initialDelaySeconds":15,"periodSeconds":20},"name":"node-disk-operator","readinessProbe":{"httpGet":{"path":"/readyz","port":8585},"initialDelaySeconds":5,"periodSeconds":10}}],"serviceAccountName":"openebs-maya-operator"}}}}
to:
Resource: "apps/v1, Resource=deployments", GroupVersionKind: "apps/v1, Kind=Deployment"
Name: "openebs-ndm-operator", Namespace: "openebs"
for: "openebs-operator.yaml": error when patching "openebs-operator.yaml": Deployment.apps "openebs-ndm-operator" is invalid: spec.selector: Invalid value: v1.LabelSelector{MatchLabels:map[string]string{"app":"openebs", "name":"openebs-ndm-operator", "openebs.io/component-name":"ndm-operator", "release":"openebs"}, MatchExpressions:[]v1.LabelSelectorRequirement(nil)}: field is immutable
Error from server (Invalid): error when applying patch:
{"metadata":{"annotations":{"kubectl.kubernetes.io/last-applied-configuration":"{\"apiVersion\":\"apps/v1\",\"kind\":\"Deployment\",\"metadata\":{\"annotations\":{},\"labels\":{\"name\":\"openebs-localpv-provisioner\",\"openebs.io/component-name\":\"openebs-localpv-provisioner\",\"openebs.io/version\":\"3.5.0\"},\"name\":\"openebs-localpv-provisioner\",\"namespace\":\"openebs\"},\"spec\":{\"replicas\":1,\"selector\":{\"matchLabels\":{\"name\":\"openebs-localpv-provisioner\",\"openebs.io/component-name\":\"openebs-localpv-provisioner\"}},\"strategy\":{\"type\":\"Recreate\"},\"template\":{\"metadata\":{\"labels\":{\"name\":\"openebs-localpv-provisioner\",\"openebs.io/component-name\":\"openebs-localpv-provisioner\",\"openebs.io/version\":\"3.5.0\"}},\"spec\":{\"containers\":[{\"args\":[\"--bd-time-out=$(BDC_BD_BIND_RETRIES)\"],\"env\":[{\"name\":\"BDC_BD_BIND_RETRIES\",\"value\":\"12\"},{\"name\":\"NODE_NAME\",\"valueFrom\":{\"fieldRef\":{\"fieldPath\":\"spec.nodeName\"}}},{\"name\":\"OPENEBS_NAMESPACE\",\"valueFrom\":{\"fieldRef\":{\"fieldPath\":\"metadata.namespace\"}}},{\"name\":\"OPENEBS_SERVICE_ACCOUNT\",\"valueFrom\":{\"fieldRef\":{\"fieldPath\":\"spec.serviceAccountName\"}}},{\"name\":\"OPENEBS_IO_ENABLE_ANALYTICS\",\"value\":\"true\"},{\"name\":\"OPENEBS_IO_INSTALLER_TYPE\",\"value\":\"openebs-operator\"},{\"name\":\"OPENEBS_IO_HELPER_IMAGE\",\"value\":\"openebs/linux-utils:3.5.0\"},{\"name\":\"OPENEBS_IO_BASE_PATH\",\"value\":\"/var/openebs/local\"}],\"image\":\"openebs/provisioner-localpv:3.4.0\",\"imagePullPolicy\":\"IfNotPresent\",\"livenessProbe\":{\"exec\":{\"command\":[\"sh\",\"-c\",\"test `pgrep -c \\\"^provisioner-loc.*\\\"` = 1\"]},\"initialDelaySeconds\":30,\"periodSeconds\":60},\"name\":\"openebs-provisioner-hostpath\"}],\"serviceAccountName\":\"openebs-maya-operator\"}}}}\n"},"labels":{"name":"openebs-localpv-provisioner","openebs.io/version":"3.5.0"}},"spec":{"selector":{"matchLabels":{"name":"openebs-localpv-provisioner","openebs.io/component-name":"openebs-localpv-provisioner"}},"template":{"metadata":{"labels":{"openebs.io/version":"3.5.0"}},"spec":{"$setElementOrder/containers":[{"name":"openebs-provisioner-hostpath"}],"containers":[{"args":["--bd-time-out=$(BDC_BD_BIND_RETRIES)"],"env":[{"name":"BDC_BD_BIND_RETRIES","value":"12"},{"name":"NODE_NAME","valueFrom":{"fieldRef":{"fieldPath":"spec.nodeName"}}},{"name":"OPENEBS_NAMESPACE","valueFrom":{"fieldRef":{"fieldPath":"metadata.namespace"}}},{"name":"OPENEBS_SERVICE_ACCOUNT","valueFrom":{"fieldRef":{"fieldPath":"spec.serviceAccountName"}}},{"name":"OPENEBS_IO_ENABLE_ANALYTICS","value":"true"},{"name":"OPENEBS_IO_INSTALLER_TYPE","value":"openebs-operator"},{"name":"OPENEBS_IO_HELPER_IMAGE","value":"openebs/linux-utils:3.5.0"},{"name":"OPENEBS_IO_BASE_PATH","value":"/var/openebs/local"}],"image":"openebs/provisioner-localpv:3.4.0","imagePullPolicy":"IfNotPresent","livenessProbe":{"exec":{"command":["sh","-c","test `pgrep -c \"^provisioner-loc.*\"` = 1"]},"initialDelaySeconds":30,"periodSeconds":60},"name":"openebs-provisioner-hostpath"}],"serviceAccountName":"openebs-maya-operator"}}}}
to:
Resource: "apps/v1, Resource=deployments", GroupVersionKind: "apps/v1, Kind=Deployment"
Name: "openebs-localpv-provisioner", Namespace: "openebs"
for: "openebs-operator.yaml": error when patching "openebs-operator.yaml": Deployment.apps "openebs-localpv-provisioner" is invalid: spec.selector: Invalid value: v1.LabelSelector{MatchLabels:map[string]string{"app":"openebs", "name":"openebs-localpv-provisioner", "openebs.io/component-name":"openebs-localpv-provisioner", "release":"openebs"}, MatchExpressions:[]v1.LabelSelectorRequirement(nil)}: field is immutable
purva@purva-VirtualBox:~/Desktop$ kubectl apply -f https://openebs.github.io/charts/openebs-operator.yaml
namespace/openebs unchanged
serviceaccount/openebs-maya-operator unchanged
clusterrole.rbac.authorization.k8s.io/openebs-maya-operator unchanged
clusterrolebinding.rbac.authorization.k8s.io/openebs-maya-operator unchanged
customresourcedefinition.apiextensions.k8s.io/blockdevices.openebs.io configured
customresourcedefinition.apiextensions.k8s.io/blockdeviceclaims.openebs.io configured
configmap/openebs-ndm-config unchanged
Warning: resource daemonsets/openebs-ndm is missing the kubectl.kubernetes.io/last-applied-configuration annotation which is required by kubectl apply. kubectl apply should only be used on resources created declaratively by either kubectl create --save-config or kubectl apply. The missing annotation will be patched automatically.
Warning: resource deployments/openebs-ndm-operator is missing the kubectl.kubernetes.io/last-applied-configuration annotation which is required by kubectl apply. kubectl apply should only be used on resources created declaratively by either kubectl create --save-config or kubectl apply. The missing annotation will be patched automatically.
deployment.apps/openebs-ndm-cluster-exporter unchanged
service/openebs-ndm-cluster-exporter-service unchanged
daemonset.apps/openebs-ndm-node-exporter unchanged
service/openebs-ndm-node-exporter-service unchanged
Warning: resource deployments/openebs-localpv-provisioner is missing the kubectl.kubernetes.io/last-applied-configuration annotation which is required by kubectl apply. kubectl apply should only be used on resources created declaratively by either kubectl create --save-config or kubectl apply. The missing annotation will be patched automatically.
storageclass.storage.k8s.io/openebs-hostpath unchanged
storageclass.storage.k8s.io/openebs-device unchanged
Error from server (Invalid): error when applying patch:
{"metadata":{"annotations":{"kubectl.kubernetes.io/last-applied-configuration":"{\"apiVersion\":\"apps/v1\",\"kind\":\"DaemonSet\",\"metadata\":{\"annotations\":{},\"labels\":{\"name\":\"openebs-ndm\",\"openebs.io/component-name\":\"ndm\",\"openebs.io/version\":\"3.5.0\"},\"name\":\"openebs-ndm\",\"namespace\":\"openebs\"},\"spec\":{\"selector\":{\"matchLabels\":{\"name\":\"openebs-ndm\",\"openebs.io/component-name\":\"ndm\"}},\"template\":{\"metadata\":{\"labels\":{\"name\":\"openebs-ndm\",\"openebs.io/component-name\":\"ndm\",\"openebs.io/version\":\"3.5.0\"}},\"spec\":{\"containers\":[{\"args\":[\"-v=4\",\"--feature-gates=\\\"GPTBasedUUID\\\"\"],\"env\":[{\"name\":\"NAMESPACE\",\"valueFrom\":{\"fieldRef\":{\"fieldPath\":\"metadata.namespace\"}}},{\"name\":\"NODE_NAME\",\"valueFrom\":{\"fieldRef\":{\"fieldPath\":\"spec.nodeName\"}}},{\"name\":\"SPARSE_FILE_DIR\",\"value\":\"/var/openebs/sparse\"},{\"name\":\"SPARSE_FILE_SIZE\",\"value\":\"10737418240\"},{\"name\":\"SPARSE_FILE_COUNT\",\"value\":\"0\"}],\"image\":\"openebs/node-disk-manager:2.1.0\",\"imagePullPolicy\":\"IfNotPresent\",\"livenessProbe\":{\"exec\":{\"command\":[\"pgrep\",\"ndm\"]},\"initialDelaySeconds\":30,\"periodSeconds\":60},\"name\":\"node-disk-manager\",\"securityContext\":{\"privileged\":true},\"volumeMounts\":[{\"mountPath\":\"/host/node-disk-manager.config\",\"name\":\"config\",\"readOnly\":true,\"subPath\":\"node-disk-manager.config\"},{\"mountPath\":\"/run/udev\",\"name\":\"udev\"},{\"mountPath\":\"/host/proc\",\"name\":\"procmount\",\"readOnly\":true},{\"mountPath\":\"/dev\",\"name\":\"devmount\"},{\"mountPath\":\"/var/openebs/ndm\",\"name\":\"basepath\"},{\"mountPath\":\"/var/openebs/sparse\",\"name\":\"sparsepath\"}]}],\"hostNetwork\":true,\"serviceAccountName\":\"openebs-maya-operator\",\"volumes\":[{\"configMap\":{\"name\":\"openebs-ndm-config\"},\"name\":\"config\"},{\"hostPath\":{\"path\":\"/run/udev\",\"type\":\"Directory\"},\"name\":\"udev\"},{\"hostPath\":{\"path\":\"/proc\",\"type\":\"Directory\"},\"name\":\"procmount\"},{\"hostPath\":{\"path\":\"/dev\",\"type\":\"Directory\"},\"name\":\"devmount\"},{\"hostPath\":{\"path\":\"/var/openebs/ndm\",\"type\":\"DirectoryOrCreate\"},\"name\":\"basepath\"},{\"hostPath\":{\"path\":\"/var/openebs/sparse\"},\"name\":\"sparsepath\"}]}},\"updateStrategy\":{\"type\":\"RollingUpdate\"}}}\n"},"labels":{"name":"openebs-ndm","openebs.io/version":"3.5.0"}},"spec":{"selector":{"matchLabels":{"name":"openebs-ndm","openebs.io/component-name":"ndm"}},"template":{"metadata":{"labels":{"openebs.io/version":"3.5.0"}},"spec":{"$setElementOrder/containers":[{"name":"node-disk-manager"}],"containers":[{"args":["-v=4","--feature-gates=\"GPTBasedUUID\""],"env":[{"name":"NAMESPACE","valueFrom":{"fieldRef":{"fieldPath":"metadata.namespace"}}},{"name":"NODE_NAME","valueFrom":{"fieldRef":{"fieldPath":"spec.nodeName"}}},{"name":"SPARSE_FILE_DIR","value":"/var/openebs/sparse"},{"name":"SPARSE_FILE_SIZE","value":"10737418240"},{"name":"SPARSE_FILE_COUNT","value":"0"}],"image":"openebs/node-disk-manager:2.1.0","imagePullPolicy":"IfNotPresent","livenessProbe":{"exec":{"command":["pgrep","ndm"]},"initialDelaySeconds":30,"periodSeconds":60},"name":"node-disk-manager","securityContext":{"privileged":true},"volumeMounts":[{"mountPath":"/host/node-disk-manager.config","name":"config","readOnly":true,"subPath":"node-disk-manager.config"},{"mountPath":"/run/udev","name":"udev"},{"mountPath":"/host/proc","name":"procmount","readOnly":true},{"mountPath":"/dev","name":"devmount"},{"mountPath":"/var/openebs/ndm","name":"basepath"},{"mountPath":"/var/openebs/sparse","name":"sparsepath"}]}],"serviceAccountName":"openebs-maya-operator"}}}}
to:
Resource: "apps/v1, Resource=daemonsets", GroupVersionKind: "apps/v1, Kind=DaemonSet"
Name: "openebs-ndm", Namespace: "openebs"
for: "https://openebs.github.io/charts/openebs-operator.yaml": error when patching "https://openebs.github.io/charts/openebs-operator.yaml": DaemonSet.apps "openebs-ndm" is invalid: spec.selector: Invalid value: v1.LabelSelector{MatchLabels:map[string]string{"app":"openebs", "component":"ndm", "name":"openebs-ndm", "openebs.io/component-name":"ndm", "release":"openebs"}, MatchExpressions:[]v1.LabelSelectorRequirement(nil)}: field is immutable
Error from server (Invalid): error when applying patch:
{"metadata":{"annotations":{"kubectl.kubernetes.io/last-applied-configuration":"{\"apiVersion\":\"apps/v1\",\"kind\":\"Deployment\",\"metadata\":{\"annotations\":{},\"labels\":{\"name\":\"openebs-ndm-operator\",\"openebs.io/component-name\":\"ndm-operator\",\"openebs.io/version\":\"3.5.0\"},\"name\":\"openebs-ndm-operator\",\"namespace\":\"openebs\"},\"spec\":{\"replicas\":1,\"selector\":{\"matchLabels\":{\"name\":\"openebs-ndm-operator\",\"openebs.io/component-name\":\"ndm-operator\"}},\"strategy\":{\"type\":\"Recreate\"},\"template\":{\"metadata\":{\"labels\":{\"name\":\"openebs-ndm-operator\",\"openebs.io/component-name\":\"ndm-operator\",\"openebs.io/version\":\"3.5.0\"}},\"spec\":{\"containers\":[{\"env\":[{\"name\":\"WATCH_NAMESPACE\",\"valueFrom\":{\"fieldRef\":{\"fieldPath\":\"metadata.namespace\"}}},{\"name\":\"POD_NAME\",\"valueFrom\":{\"fieldRef\":{\"fieldPath\":\"metadata.name\"}}},{\"name\":\"SERVICE_ACCOUNT\",\"valueFrom\":{\"fieldRef\":{\"fieldPath\":\"spec.serviceAccountName\"}}},{\"name\":\"OPERATOR_NAME\",\"value\":\"node-disk-operator\"},{\"name\":\"CLEANUP_JOB_IMAGE\",\"value\":\"openebs/linux-utils:3.5.0\"}],\"image\":\"openebs/node-disk-operator:2.1.0\",\"imagePullPolicy\":\"IfNotPresent\",\"livenessProbe\":{\"httpGet\":{\"path\":\"/healthz\",\"port\":8585},\"initialDelaySeconds\":15,\"periodSeconds\":20},\"name\":\"node-disk-operator\",\"readinessProbe\":{\"httpGet\":{\"path\":\"/readyz\",\"port\":8585},\"initialDelaySeconds\":5,\"periodSeconds\":10}}],\"serviceAccountName\":\"openebs-maya-operator\"}}}}\n"},"labels":{"name":"openebs-ndm-operator","openebs.io/version":"3.5.0"}},"spec":{"selector":{"matchLabels":{"name":"openebs-ndm-operator","openebs.io/component-name":"ndm-operator"}},"template":{"metadata":{"labels":{"name":"openebs-ndm-operator","openebs.io/version":"3.5.0"}},"spec":{"$setElementOrder/containers":[{"name":"node-disk-operator"}],"containers":[{"env":[{"name":"WATCH_NAMESPACE","valueFrom":{"fieldRef":{"fieldPath":"metadata.namespace"}}},{"name":"POD_NAME","valueFrom":{"fieldRef":{"fieldPath":"metadata.name"}}},{"name":"SERVICE_ACCOUNT","valueFrom":{"fieldRef":{"fieldPath":"spec.serviceAccountName"}}},{"name":"OPERATOR_NAME","value":"node-disk-operator"},{"name":"CLEANUP_JOB_IMAGE","value":"openebs/linux-utils:3.5.0"}],"image":"openebs/node-disk-operator:2.1.0","imagePullPolicy":"IfNotPresent","livenessProbe":{"httpGet":{"path":"/healthz","port":8585},"initialDelaySeconds":15,"periodSeconds":20},"name":"node-disk-operator","readinessProbe":{"httpGet":{"path":"/readyz","port":8585},"initialDelaySeconds":5,"periodSeconds":10}}],"serviceAccountName":"openebs-maya-operator"}}}}
to:
Resource: "apps/v1, Resource=deployments", GroupVersionKind: "apps/v1, Kind=Deployment"
Name: "openebs-ndm-operator", Namespace: "openebs"
for: "https://openebs.github.io/charts/openebs-operator.yaml": error when patching "https://openebs.github.io/charts/openebs-operator.yaml": Deployment.apps "openebs-ndm-operator" is invalid: spec.selector: Invalid value: v1.LabelSelector{MatchLabels:map[string]string{"app":"openebs", "name":"openebs-ndm-operator", "openebs.io/component-name":"ndm-operator", "release":"openebs"}, MatchExpressions:[]v1.LabelSelectorRequirement(nil)}: field is immutable
Error from server (Invalid): error when applying patch:
{"metadata":{"annotations":{"kubectl.kubernetes.io/last-applied-configuration":"{\"apiVersion\":\"apps/v1\",\"kind\":\"Deployment\",\"metadata\":{\"annotations\":{},\"labels\":{\"name\":\"openebs-localpv-provisioner\",\"openebs.io/component-name\":\"openebs-localpv-provisioner\",\"openebs.io/version\":\"3.5.0\"},\"name\":\"openebs-localpv-provisioner\",\"namespace\":\"openebs\"},\"spec\":{\"replicas\":1,\"selector\":{\"matchLabels\":{\"name\":\"openebs-localpv-provisioner\",\"openebs.io/component-name\":\"openebs-localpv-provisioner\"}},\"strategy\":{\"type\":\"Recreate\"},\"template\":{\"metadata\":{\"labels\":{\"name\":\"openebs-localpv-provisioner\",\"openebs.io/component-name\":\"openebs-localpv-provisioner\",\"openebs.io/version\":\"3.5.0\"}},\"spec\":{\"containers\":[{\"args\":[\"--bd-time-out=$(BDC_BD_BIND_RETRIES)\"],\"env\":[{\"name\":\"BDC_BD_BIND_RETRIES\",\"value\":\"12\"},{\"name\":\"NODE_NAME\",\"valueFrom\":{\"fieldRef\":{\"fieldPath\":\"spec.nodeName\"}}},{\"name\":\"OPENEBS_NAMESPACE\",\"valueFrom\":{\"fieldRef\":{\"fieldPath\":\"metadata.namespace\"}}},{\"name\":\"OPENEBS_SERVICE_ACCOUNT\",\"valueFrom\":{\"fieldRef\":{\"fieldPath\":\"spec.serviceAccountName\"}}},{\"name\":\"OPENEBS_IO_ENABLE_ANALYTICS\",\"value\":\"true\"},{\"name\":\"OPENEBS_IO_INSTALLER_TYPE\",\"value\":\"openebs-operator\"},{\"name\":\"OPENEBS_IO_HELPER_IMAGE\",\"value\":\"openebs/linux-utils:3.5.0\"},{\"name\":\"OPENEBS_IO_BASE_PATH\",\"value\":\"/var/openebs/local\"}],\"image\":\"openebs/provisioner-localpv:3.4.0\",\"imagePullPolicy\":\"IfNotPresent\",\"livenessProbe\":{\"exec\":{\"command\":[\"sh\",\"-c\",\"test `pgrep -c \\\"^provisioner-loc.*\\\"` = 1\"]},\"initialDelaySeconds\":30,\"periodSeconds\":60},\"name\":\"openebs-provisioner-hostpath\"}],\"serviceAccountName\":\"openebs-maya-operator\"}}}}\n"},"labels":{"name":"openebs-localpv-provisioner","openebs.io/version":"3.5.0"}},"spec":{"selector":{"matchLabels":{"name":"openebs-localpv-provisioner","openebs.io/component-name":"openebs-localpv-provisioner"}},"template":{"metadata":{"labels":{"openebs.io/version":"3.5.0"}},"spec":{"$setElementOrder/containers":[{"name":"openebs-provisioner-hostpath"}],"containers":[{"args":["--bd-time-out=$(BDC_BD_BIND_RETRIES)"],"env":[{"name":"BDC_BD_BIND_RETRIES","value":"12"},{"name":"NODE_NAME","valueFrom":{"fieldRef":{"fieldPath":"spec.nodeName"}}},{"name":"OPENEBS_NAMESPACE","valueFrom":{"fieldRef":{"fieldPath":"metadata.namespace"}}},{"name":"OPENEBS_SERVICE_ACCOUNT","valueFrom":{"fieldRef":{"fieldPath":"spec.serviceAccountName"}}},{"name":"OPENEBS_IO_ENABLE_ANALYTICS","value":"true"},{"name":"OPENEBS_IO_INSTALLER_TYPE","value":"openebs-operator"},{"name":"OPENEBS_IO_HELPER_IMAGE","value":"openebs/linux-utils:3.5.0"},{"name":"OPENEBS_IO_BASE_PATH","value":"/var/openebs/local"}],"image":"openebs/provisioner-localpv:3.4.0","imagePullPolicy":"IfNotPresent","livenessProbe":{"exec":{"command":["sh","-c","test `pgrep -c \"^provisioner-loc.*\"` = 1"]},"initialDelaySeconds":30,"periodSeconds":60},"name":"openebs-provisioner-hostpath"}],"serviceAccountName":"openebs-maya-operator"}}}}
to:
Resource: "apps/v1, Resource=deployments", GroupVersionKind: "apps/v1, Kind=Deployment"
Name: "openebs-localpv-provisioner", Namespace: "openebs"
for: "https://openebs.github.io/charts/openebs-operator.yaml": error when patching "https://openebs.github.io/charts/openebs-operator.yaml": Deployment.apps "openebs-localpv-provisioner" is invalid: spec.selector: Invalid value: v1.LabelSelector{MatchLabels:map[string]string{"app":"openebs", "name":"openebs-localpv-provisioner", "openebs.io/component-name":"openebs-localpv-provisioner", "release":"openebs"}, MatchExpressions:[]v1.LabelSelectorRequirement(nil)}: field is immutable
purva@purva-VirtualBox:~/Desktop$ 
purva@purva-VirtualBox:~/Desktop$ 
purva@purva-VirtualBox:~/Desktop$ 
purva@purva-VirtualBox:~/Desktop$ kubectl config set-context csi_context --cluster=c1 --user=shrinirva --namespace=openebs
Context "csi_context" modified.
purva@purva-VirtualBox:~/Desktop$ 
purva@purva-VirtualBox:~/Desktop$ 
purva@purva-VirtualBox:~/Desktop$ kubectl config use-context csi_context
Switched to context "csi_context".
purva@purva-VirtualBox:~/Desktop$ helm ls -n openebs
Error: Kubernetes cluster unreachable: Get "http://localhost:8080/version": dial tcp 127.0.0.1:8080: connect: connection refused
purva@purva-VirtualBox:~/Desktop$ minikube status
minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured

purva@purva-VirtualBox:~/Desktop$ helm update repo
Error: unknown command "update" for "helm"
Run 'helm --help' for usage.
purva@purva-VirtualBox:~/Desktop$ helm repo update
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "openebs" chart repository
Update Complete. ⎈Happy Helming!⎈
purva@purva-VirtualBox:~/Desktop$ helm ls -n openebs
Error: Kubernetes cluster unreachable: Get "http://localhost:8080/version": dial tcp 127.0.0.1:8080: connect: connection refused
purva@purva-VirtualBox:~/Desktop$ 
purva@purva-VirtualBox:~/Desktop$ 
purva@purva-VirtualBox:~/Desktop$ helm ls -n openebs
Error: Kubernetes cluster unreachable: Get "http://localhost:8080/version": dial tcp 127.0.0.1:8080: connect: connection refused
purva@purva-VirtualBox:~/Desktop$ helm install openebs --namespace openebs openebs/openebs --create-namespace
Error: INSTALLATION FAILED: Kubernetes cluster unreachable: Get "http://localhost:8080/version": dial tcp 127.0.0.1:8080: connect: connection refused
purva@purva-VirtualBox:~/Desktop$ helm install openebs --namespace openebs openebs/openebs --create-namespace --set cstor.enabled=true
Error: INSTALLATION FAILED: Kubernetes cluster unreachable: Get "http://localhost:8080/version": dial tcp 127.0.0.1:8080: connect: connection refused
purva@purva-VirtualBox:~/Desktop$ helm repo add openebs https://openebs.github.io/charts
helm repo update
"openebs" already exists with the same configuration, skipping
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "openebs" chart repository
Update Complete. ⎈Happy Helming!⎈
purva@purva-VirtualBox:~/Desktop$ helm install openebs --namespace openebs openebs/openebs --create-namespace
Error: INSTALLATION FAILED: Kubernetes cluster unreachable: Get "http://localhost:8080/version": dial tcp 127.0.0.1:8080: connect: connection refused
purva@purva-VirtualBox:~/Desktop$ kubectl version
Client Version: v1.29.2
Kustomize Version: v5.0.4-0.20230601165947-6ce0bf390ce3
The connection to the server localhost:8080 was refused - did you specify the right host or port?
purva@purva-VirtualBox:~/Desktop$ helm install openebs --namespace openebs openebs/openebs --create-namespace --kube-api-server <api_server_address>:<port>
bash: syntax error near unexpected token `newline'
purva@purva-VirtualBox:~/Desktop$ 
purva@purva-VirtualBox:~/Desktop$ 
purva@purva-VirtualBox:~/Desktop$ 
purva@purva-VirtualBox:~/Desktop$ 
purva@purva-VirtualBox:~/Desktop$ helm repo add openebs https://openebs.github.io/charts
"openebs" already exists with the same configuration, skipping
purva@purva-VirtualBox:~/Desktop$ helm repo update
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "openebs" chart repository
Update Complete. ⎈Happy Helming!⎈
purva@purva-VirtualBox:~/Desktop$ helm install openebs --namespace openebs openebs/openebs --create-namespace
Error: INSTALLATION FAILED: Kubernetes cluster unreachable: Get "http://localhost:8080/version": dial tcp 127.0.0.1:8080: connect: connection refused
purva@purva-VirtualBox:~/Desktop$ helm ls -n openebs
Error: Kubernetes cluster unreachable: Get "http://localhost:8080/version": dial tcp 127.0.0.1:8080: connect: connection refused
purva@purva-VirtualBox:~/Desktop$ helm ls -n open_ebs
Error: Kubernetes cluster unreachable: Get "http://localhost:8080/version": dial tcp 127.0.0.1:8080: connect: connection refused
purva@purva-VirtualBox:~/Desktop$ helm ls -n openebs
Error: Kubernetes cluster unreachable: Get "http://localhost:8080/version": dial tcp 127.0.0.1:8080: connect: connection refused
purva@purva-VirtualBox:~/Desktop$ minikube status
minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured

purva@purva-VirtualBox:~/Desktop$ minikube start
😄  minikube v1.32.0 on Ubuntu 22.04 (vbox/amd64)
✨  Using the docker driver based on existing profile
👍  Starting control plane node minikube in cluster minikube
🚜  Pulling base image ...
🏃  Updating the running docker "minikube" container ...
🐳  Preparing Kubernetes v1.28.3 on Docker 24.0.7 ...
🔎  Verifying Kubernetes components...
    ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
🌟  Enabled addons: storage-provisioner, default-storageclass
🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default
purva@purva-VirtualBox:~/Desktop$ helm ls -n openebs
NAME   	NAMESPACE	REVISION	UPDATED                                	STATUS  	CHART         	APP VERSION
openebs	openebs  	1       	2024-03-09 17:12:52.496835282 +0530 IST	deployed	openebs-3.10.0	3.10.0     
purva@purva-VirtualBox:~/Desktop$ 
