#!/bin/bash

# Command 1
cd ../deploy/

# Command 2
echo "Applying Secrets..."
sudo kubectl create -f csi-secret.yaml

# Command 3
echo "Creating pod  Provisiner.."
sudo kubectl create -f provisioner.yaml


# Command 4
echo "Deploying driver.."
sudo kubectl create -f driver.yaml


# Command 5
echo "Creating csi-s3..."
sudo kubectl create -f csi-s3.yaml

# Command 5
echo "Creating Storage Class.."
sudo kubectl create -f pod-configuration/storageclass.yaml

# Command 5
echo "Creating PVC..."
sudo kubectl create -f pod-configuration/pvc.yaml

# Command 5
echo "Checking Bound status"
sudo kubectl get pvc csi-s3-pvc


