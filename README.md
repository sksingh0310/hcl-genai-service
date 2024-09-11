# Deploying FastAPI Application to Azure Kubernetes Service (AKS)

This guide provides instructions to deploy a FastAPI application to Azure Kubernetes Service (AKS) using Docker Hub as the image source.

## Prerequisites

- Azure account
- Azure CLI installed
- kubectl installed and configured
- Docker image available on Docker Hub (e.g., `sksingh031/fastapi-app:latest`)
- Kubernetes configuration files: `deployment.yaml` and `service.yaml`

## Steps to Deploy

### 1. Create an AKS Cluster

If you haven't already created an AKS cluster, use the Azure CLI to create one:

bash
az aks create --resource-group <your-resource-group> --name <your-aks-cluster> --node-count 3 --enable-addons monitoring --generate-ssh-keys


Replace `<your-resource-group>` and `<your-aks-cluster>` with your desired resource group and cluster name.

### 2. Connect to Your AKS Cluster

Configure `kubectl` to connect to your AKS cluster:

bash
az aks get-credentials --resource-group <your-resource-group> --name <your-aks-cluster>


### 3. Deploy Your Application

Use the `kubectl` command to apply your Kubernetes configuration files:

1. **Deploy the application**:
bash
kubectl apply -f deployment.yaml


2. **Expose the application**:
bash
kubectl apply -f service.yaml


### 4. Monitor and Access Your Application

- **Check the status of your deployment**:
bash
kubectl get pods


- **Check the status of your service**:
bash
kubectl get services


- **Access your application**:
  Once the service is up and running, it will be assigned an external IP address. Use this IP address to access your FastAPI application.

## Conclusion

By following these steps, you can successfully deploy your FastAPI application to Azure Kubernetes Service using a Docker image from Docker Hub. Adjust the configurations in your `deployment.yaml` and `service.yaml` files as needed for your specific application requirements.