purva@purva-VirtualBox:~/Desktop$ curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 89.3M  100 89.3M    0     0  3253k      0  0:00:28  0:00:28 --:--:-- 3324k


purva@purva-VirtualBox:~/Desktop$ minikube start
😄  minikube v1.32.0 on Ubuntu 22.04 (vbox/amd64)
👎  Unable to pick a default driver. Here is what was considered, in preference order:
    ▪ docker: Not healthy: "docker version --format {{.Server.Os}}-{{.Server.Version}}:{{.Server.Platform.Name}}" exit status 1: permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.44/version": dial unix /var/run/docker.sock: connect: permission denied
    ▪ docker: Suggestion: Add your user to the 'docker' group: 'sudo usermod -aG docker $USER && newgrp docker' <https://docs.docker.com/engine/install/linux-postinstall/>
    ▪ kvm2: Not healthy: libvirt group membership check failed:
user is not a member of the appropriate libvirt group
    ▪ kvm2: Suggestion: Check that libvirtd is properly installed and that you are a member of the appropriate libvirt group (remember to relogin for group changes to take effect!) <https://minikube.sigs.k8s.io/docs/reference/drivers/kvm2/>
    ▪ podman: Not healthy: "sudo -n -k podman version --format {{.Version}}" exit status 1: sudo: a password is required
    ▪ podman: Suggestion: Add your user to the 'sudoers' file: 'purva ALL=(ALL) NOPASSWD: /usr/bin/podman' , or run 'minikube config set rootless true' <https://podman.io>
💡  Alternatively you could install one of these drivers:
    ▪ qemu2: Not installed: exec: "qemu-system-x86_64": executable file not found in $PATH
    ▪ virtualbox: Not installed: unable to find VBoxManage in $PATH



purva@purva-VirtualBox:~/Desktop$ sudo apt install conntrack
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following NEW packages will be installed:
  conntrack
0 upgraded, 1 newly installed, 0 to remove and 29 not upgraded.
Need to get 33.5 kB of archives.
After this operation, 104 kB of additional disk space will be used.
Get:1 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 conntrack amd64 1:1.4.6-2build2 [33.5 kB]
Fetched 33.5 kB in 3s (10.4 kB/s)    
Selecting previously unselected package conntrack.
(Reading database ... 202799 files and directories currently installed.)
Preparing to unpack .../conntrack_1%3a1.4.6-2build2_amd64.deb ...
Unpacking conntrack (1:1.4.6-2build2) ...
Setting up conntrack (1:1.4.6-2build2) ...
Processing triggers for man-db (2.10.2-1) ...


purva@purva-VirtualBox:~/Desktop$ sudo usermod -aG docker $USER && newgrp docker

purva@purva-VirtualBox:~/Desktop$ minikube start
😄  minikube v1.32.0 on Ubuntu 22.04 (vbox/amd64)
✨  Automatically selected the docker driver. Other choices: ssh, none
📌  Using Docker driver with root privileges
👍  Starting control plane node minikube in cluster minikube
🚜  Pulling base image ...
💾  Downloading Kubernetes v1.28.3 preload ...
    > preloaded-images-k8s-v18-v1...:  403.35 MiB / 403.35 MiB  100.00% 1.97 Mi
    > gcr.io/k8s-minikube/kicbase...:  453.90 MiB / 453.90 MiB  100.00% 2.00 Mi
🔥  Creating docker container (CPUs=2, Memory=2200MB) ...
🐳  Preparing Kubernetes v1.28.3 on Docker 24.0.7 ...
    ▪ Generating certificates and keys ...
    ▪ Booting up control plane ...
    ▪ Configuring RBAC rules ...
🔗  Configuring bridge CNI (Container Networking Interface) ...
    ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
🔎  Verifying Kubernetes components...
🌟  Enabled addons: storage-provisioner, default-storageclass
💡  kubectl not found. If you need it, try: 'minikube kubectl -- get pods -A'
🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default


purva@purva-VirtualBox:~/Desktop$ minikube status
minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured

