#!/bin/bash

## Prepairing the environment ##
sudo apt-get upgrade
sudo spt-get install docker
sudo service docker start
sudo apt-get install apt-transport-https
sudo apt-get upgrade
sudo apt install virtualbox virtualbox-ext-pack

wget https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
chmod +x minikube-linux-amd64
sudo mv minikube-linux-amd64 /usr/local/bin/minikube

curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl
minikube start
####


cd /
git clone ---link
cd /pythonproject

minikube stop
minikube delete
minikube start
minikube addons enable ingress
eval $(minikube docker-env)
docker build -f /pythonprojecy/Dockerfile -t pythonproject:latest . # create the image
docker run -p 5001:5000 -d pythonproject # run image into the container

kubectl apply -f /pythonprojec/kubernetes.yaml
kubectl appy -f /pythonproject/ingress.yaml





