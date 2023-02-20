#!/bin/bash

# This script will build a local kubernetes cluster on your machine
# the cluster will have 1 master node and 3 workers (agent) nodes
# and one local registry

# Create the cluster along with a local registry running on port 5432

#
if ! docker ps &>/dev/null; then
    echo "Please Make sure docker is installed and running on your system"
    echo "Please check you also have permision to run docker"
    exit 2
else
    echo "---"
    echo "Docker is running, carry on..."
    echo
fi

# Check for k3d
if ! which k3d &>/dev/null; then
    echo "Please Make sure k3d is installed and running on your system"
    echo "Please use this link to installed it"
    echo "Link: https://k3d.io/v5.4.7/#installation"
    exit 2
else
    echo "---"
    echo "K3D is installed, carrt on..."
    echo "---"
    echo
fi

# Create the cluster if not found.
if ! k3d cluster ls | grep -q k8s-local; then
    echo "We're creating a k8s cluster for you...,"
    echo "This will take a minute or two :)"
    cd ..;
    export SL_API="$PWD"
    cd - || exit
    echo "------"
    echo "slapi: $SL_API"
    echo "------"
    if k3d cluster create -c k3d-config.yaml --registry-create k8s-local-registry:0.0.0.0:5432; then
        echo "K3d is now running"
        echo "Please wait a moment for the cluster to be ready."
        sleep 60
    fi
else
    echo "---"
    echo "Your cluster is already running"
    echo "---"
    echo
fi

# Double check the registry is created.
if ! k3d registry ls | grep -q k8s-local-registry; then
    echo "---"
    echo "We're creating a local registry for your local kubernetes cluster"
    echo "---"
    if k3d registry create k8s-local-registry --port 0.0.0.0:5432; then
        echo "The registry has been created succesfully"
    fi
else
    echo "The local registry for k8s is already created."
    echo "---"
fi

# Building the container sl-api images
if ! docker image ls localhost:5432/dzsaintsurin/sl-api:1 | grep -qE 'localhost:5432/dzsaintsurin/sl-api\s+1.0'; then
    echo "---"
    echo "Created the docker image for the app"
    cd ../ && docker build -t localhost:5432/dzsaintsurin/sl-api:1.0 . 
else
    echo "---"
    echo "The correct image is on your system"
fi

# Push the image to the local k3d kubernetes cluster
echo "Pushing the docker image to your k8s registry"
if docker push localhost:5432/dzsaintsurin/sl-api:1.0 ; then
    echo "---"
    echo "the app image has been added to your registry"
else
    echo "---"
    echo "there was a problem adding the sl-api image to your k8s registry"
    exit 2
fi
