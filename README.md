VRTS_uconnect_hackathon_2024

OpenEBS S3 Caching with Kubernetes -

This describes how to set up OpenEBS S3cache, a CSI driver, for S3 object caching within the Kubernetes cluster. By leveraging S3cache, we can potentially improve the performance of our applications by caching frequently accessed data locally within the cluster, reducing the need to fetch data directly from S3.

Prerequisites:

    Kubernetes cluster (e.g., Minikube )
    S3-compatible object storage account (e.g., AWS S3) with appropriate bucket creation permissions
    API credentials (access key ID and secret access key) for programmatic access to your S3 bucket

Software Requirements:

    OpenEBS (version compatible with your Kubernetes cluster)
    kubectl command-line tool

  Steps:
    Cloud Storage Setup:
        Create a bucket within your chosen S3-compatible object storage account to store the data we want to cache.
        Obtain API credentials with permissions to access and potentially modify data in the S3 bucket.

    Kubernetes Cluster Deployment:
        A deployment method for your Kubernetes cluster:
            Local Cluster (Minikube): Installation of minikube

    Choose a CSI Driver Implementation:

    OpenEBS S3cache- 
      OpenEBS is an open-source project that provides a suite of storage solutions specifically designed for containerized workloads running on Kubernetes. It offers a cloud-native approach to managing persistent storage for stateful applications within your Kubernetes cluster.


    Create S3 Access Secret:

    Use kubectl create secret to create a Kubernetes secret named s3-credentials to store your S3 access credentials securely:
    
    kubectl create secret generic s3-credentials \
      --from literal=accessKey=<YOUR_S3_ACCESS_KEY_ID> \
      --from-literal=secretKey=<YOUR_S3_SECRET_ACCESS_KEY>


      

