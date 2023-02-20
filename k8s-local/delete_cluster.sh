#!/bin/bash

# Delete the cluster
if k3d cluster ls | grep -q k8s-local; then
    k3d cluster delete k8s-local
fi

# Delete the cluster
if k3d registry ls | grep -q k8s-local; then
    k3d registry delete k8s-local-registry
fi
