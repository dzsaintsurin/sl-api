```
 ____   _              _     ____  ___
/ ___| | |            / \   |  _ \|_ _|
\___ \ | |    _____  / _ \  | |_) || |
 ___) || |___|_____|/ ___ \ |  __/ | |
|____/ |_____|     /_/   \_\|_|   |___|
```
# SL-API

SL-API is a web application that uses Python and FastAPI framework to fetch data from a public API (Reqres).

## App components

The app consists of a few main parts:

- The Web-API: This is the core of the app that handles requests and responses. It is written in Python and located at sl-api-app folder.
- The Dockerfile: This is a file that defines how to build a Docker image for the app. It is located at the root of the repo.
- There is also a makefile to automate the building and running process for the different provided environment(docker, docker-compose, and kubernertes, I am using k3d an easy and quiker way to build a kubernetes cluster on your local machine, something similar to kind)

#

## How to quickly get started

To run the app locally, you need to have Docker installed on your machine. Then follow these steps:

1. Clone this repo to your local machine.
2. Navigate to the repo folder and run `make run-deploy-docker`. This will to build the Docker image and start the container with the app.
3. Visit `http://localhost:8070` to see the documentation of the Web-API.

Enjoy!

#

## Other ways to run the application.
Besides the above, the app can be run via docker-compose or kubernetes. There is a makefile automation in place to ease the process. To deploy via docker-compose or k8s, just follow the steps below:

#

## How to run the application via docker-compose.

1. Navigate to the repo folder and run `make run-deploy-docker`. This will to build the Docker image and start the container with the app.
2. Visit [http://localhost:8090]() to see the documentation of the Web-API.

Enjoy!
#

## How to run the application via Kubernetes.
To run the exact make file, a few packages needs to be installed on your system:
- [docker](./k8s-local/README.md#k8s-local-setup)
- [K3D](./k8s-local/README.md#k8s-local-setup)
- [kubectl](./k8s-local/README.md#k8s-local-setup)

1. Navigate to the repo folder and run `make run-deploy-k8s`. This will to build the Docker image and start the container with the app.
2. Visit [http://localhost:8080]() to see the documentation of the Web-API.

Enjoy!



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
### [Back To The Root Repository](https://github.com/dzsaintsurin/sl-api)