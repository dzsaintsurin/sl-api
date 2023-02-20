```
 ____   _              _     ____  ___
/ ___| | |            / \   |  _ \|_ _|
\___ \ | |    _____  / _ \  | |_) || |
 ___) || |___|_____|/ ___ \ |  __/ | |
|____/ |_____|     /_/   \_\|_|   |___|
```
# SL-API

- SL-API is a simple web-app written in Python and FastAPI web Framework.
The application use a public api url: [Reqres](https://reqres.in/api) to retrieve data.

- The code of the application are located in [sl-api-app](./sl-api-app)

#

## App components:
1. The Web-API is the core application written in Python located at [sl-api-app](./sl-api-app). The application makes use of [FastAPI](http://fastapi.tiangolo.com) Web Framework to create a Resful API.
2. A kubernetes cluster build using k3d (dubernetes on Docker) at [k8s-local](./k8s-local)
3. A [Dockerfile](./Dockerfile) use to build the container image that will be use for docker and kubernetes deployment.
4. A [docker-compose.yml](./docker-compose.yml) file for docker-comose deployment.
5. There is a (makefile)[./makefile] for automated deployment. This makefile can be use to deploy the application via docker, docker-compose and kubernetes.

# 
## A Note about the Dockerfile
In the Dockerfile, I chose not to include the Python application. The Python application is linked to the container image at the deployment time. while this is very minimal with just a few files, I found some docker-image getting very large when the application are hard coded within the container image. Some Container image can be in the Gb size.

This container image has only the Python base image and the needed library installed. 

Dockerfile:
```sh=
FROM python:3.10.10-alpine3.17

WORKDIR /app

COPY sl-api-app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["python", "/app/sl-api/main.py"]

```

If we prefer to have the Python code built into the docker image, change the above lines of the Dockerfile to this one below:
```sh=
FROM python:3.10.10-alpine3.17

WORKDIR /app

COPY sl-api-app/requirements.txt .

COPY sl-api-app /app/sl-api/app    

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["python", "/app/sl-api/main.py"]

```

#

## How to deploy the application.
To quickly deploy the application, there is a makefile in the root of the repo. The application can be deployed with either:
- Docker
- Docker-Compose
- Kubernetes

The makefile will take steps of building the docker image if needed, created the k8s cluster, namespace, deployment, services, etc.., and teardown those env at the end of the process. Please follow the steps below to get started with the deployment.

#

## Deploy the application (SL-API) Via Docker, (the fastest way to get started).
Please make sure docker is installed on your system.
From the root of the repository, run the command below.
```sh=
make run-deploy-docker
```
To access the application when deployed with `make run-deploy-docker`, click on this link: http://localhost:8070

#

### Remove the Docker deployment
To delete the deployment created via plain docker, from the root of the repository, run the command below.
```sh=
make delete-deploy-doker
```

#

### Deploy the application (SL-API) Via Docker-Compose.
Make sure both docker and docker-compose are installed on your machine.
From the root of the repository, run the command below.
```sh=
make run-deploy-dcompose
```
To access the application from your local machine when deployed via docker-compose with `make run-deploy-dcompose`, use this url: http://localhost:8090

#

### Remove the Docker-Compose deployment.
To delete the docker-comppose deployment, from the root of the repository, run the command below.
```sh=
make delete-deploy-dcompose
```
#

### Deploy the application (SL-API) Via Kubernetes.
To run the exact make file, a few packages needs to be installed on your system:
- [docker](./k8s-local/README.md#k8s-local-setup)
- [K3D](./k8s-local/README.md#k8s-local-setup)
- [kubectl](./k8s-local/README.md#k8s-local-setup)

To deploy the application via kubernetes on the provided cluster, the root repository, run the command below.
```sh=
make run-deploy-k8s
```
To access the application from your local machine when deployed on the provided k8s cluster with make file command `make run-deploy-k8s`, use this url: http://localhost:8080


#

### Remove the k8s deployment
```sh=
make delete-deploy-k8s
```

#

Each of those provided url above will take you to the same Swagger API page of the application.

There are implementation for each of the Vebs provided by the public API [Reqres](https://reqres.in/api)

# 
### [Back To The Root Repository](https://github.com/dzsaintsurin/sl-api)