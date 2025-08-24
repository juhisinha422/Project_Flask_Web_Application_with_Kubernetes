# 🚀 Dockerized Flask App Deployment on AWS EKS using Kubernetes & DockerHub

This project demonstrates how to containerize a simple Flask application, push it to DockerHub, and deploy it on an **Amazon EKS (Elastic Kubernetes Service)** cluster using `kubectl`.

---

## 📁 Project Structure

```bash
├── app.py             # Main Flask application
├── Dockerfile         # Dockerfile for building the image
├── requirements.txt   # Python dependencies
└── README.md          # This file
```

## ⚙️ Tech Stack

- Python Flask 🐍  
- Docker 🐳  
- DockerHub 📦  
- AWS EKS ☁️  
- kubectl ⚙️

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/juhisinha422/Project_Flask_Web_Application_with_Kubernetes.git
cd k8s-flask-eks
```

### 2. Build and Test Docker Image Locally

```bash
docker build -t my_flask_app:v1 .
docker run -itd -p 5000:5000 --name flask_app my_flask_app:v1
curl http://localhost:5000/home
```

### 3. Push Image to DockerHub

```bash
docker tag my_flask_app:v1 juhisinha/k8s-flask-app-project:v1
docker login
docker push juhisinha/k8s-flask-app-project:v1
```

### 4. Create EKS Cluster (via eksctl)

```bash
eksctl create cluster --name MyCluster --version 1.29 --region ap-south-1 --nodegroup-name linux-nodes --node-type t2.micro --nodes 2 --managed
NOTE: We can create cluster using KIND also.
```

### 5. Deploy on Kubernetes

```bash
kubectl create deployment myflaskappdeploy --image=juhisinha/k8s-flask-app-project:v1
kubectl expose deployment myflaskappdeploy --type=NodePort --port=5000 --target-port=5000
```

### 6. Access the Application

```bash
kubectl get svc
```

### Access the Application

Use the EXTERNAL-IP of your node and the NODE-PORT to access:
- http://NODE-EXTERNAL-IP:NODE-PORT/home

## 📸 Sample Output
```vnet
Welcome to my Flask app..., 
My hostname is : myflaskappdeploy-69cbb486b9-4qqmc, 
My ip : 192.168.0.x

![Flask App Screenshot](https://raw.githubusercontent.com/juhisinha422/Project_Flask_Web_Application_with_Kubernetes/main/images/image.png)
```

## 🔍 Useful Commands

```bash
kubectl get nodes
kubectl get pods
kubectl get svc
kubectl describe pod <pod-name>
kubectl logs <pod-name>
```

## 🧠 What I Learned

- Docker Image Creation and Push  
- AWS EKS Cluster Setup with eksctl  
- Deploying Flask App in Kubernetes using kubectl  
- Networking with NodePort Service  
- Accessing App via External Node IP

## 🔗 Links

- 📦 DockerHub: [juhisinha/k8s-flask-app-project](https://hub.docker.com/r/juhisinha/k8s-flask-app-project)
- ☁️ AWS: [Amazon EKS](https://aws.amazon.com/eks/)

## 🙌 Author

**Juhi Sinha**  
DevOps Engineer | DevOps & Cloud Enthusiast  

