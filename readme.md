# Veritas U-connect Hackathon
## Kubernetes installation

DEMO LINK - https://youtu.be/XlQEvyUBn2Y

### Requirements

To get this working, you'll need a few things:

* Kubernetes version 1.17 or newer
* Make sure Kubernetes allows privileged containers
* Your Docker daemon must allow shared mounts (check the systemd flag `MountFlags=shared`)


### Manual installation

Now, if you're feeling adventurous and want to install it manually, here's what you gotta do:

#### 1. Setting up your S3 credentials

First, you need to create a secret with your S3 credentials. Check it out:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: csi-s3-secret
  namespace: kube-system
stringData:
  accessKeyID: <YOUR_ACCESS_KEY_ID>
  secretAccessKey: <YOUR_SECRET_ACCESS_KEY>
  endpoint: <S3_ENDPOINT>
```

Make sure to replace `<YOUR_ACCESS_KEY_ID>` and `<YOUR_SECRET_ACCESS_KEY>` with your actual S3 credentials. 

#### 2. Deploying the driver

Next up, you gotta deploy the driver. Here's the command:

```bash
cd deploy/kubernetes
kubectl create -f provisioner.yaml
kubectl create -f driver.yaml
kubectl create -f csi-s3.yaml
```

If you're updating from a previous version that used `attacher.yaml`, you can safely delete resources created from that file.

#### 3. Creating the storage class

Now, create the storage class like so:

```bash
kubectl create -f examples/storageclass.yaml
```


