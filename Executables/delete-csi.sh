#!/bin/bash

# Command 5
echo "Deleting POD..."
sudo kubectl delete pod s3fs-test-nginx

# Command 1
cd ../deploy/

# Command 2
echo "Deleting Secrets..."
sudo kubectl delete -f csi-secret.yaml

# Command 3
echo "Deleting pod  Provisiner.."
sudo kubectl delete -f provisioner.yaml


# Command 4
echo "Deleting driver.."
sudo kubectl delete -f driver.yaml


# Command 5
echo "Deleting csi-s3..."
sudo kubectl delete -f csi-s3.yaml

# Command 5
echo "Deleting Storage Class.."
sudo kubectl delete -f pod-configuration/storageclass.yaml

# Command 5
echo "Deleting PVC..."
sudo kubectl delete -f pod-configuration/pvc.yaml

