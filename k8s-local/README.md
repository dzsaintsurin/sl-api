# k8s-local setup

## Kubernetes within k3d

K3d use Kubernetes inside of docker, To use k3d, Docker needs to be install on your local machine.
* [Docker Desktop on Mac](https://docs.docker.com/desktop/install/mac-install/)
* [Docker Desktop on Linux](https://docs.docker.com/desktop/install/linux-install/)
* [Docker Desktopon Windows](https://docs.docker.com/desktop/install/windows-install/)

K3D and kubectl need to be installed on your local machine. 
* [Install Docker]()
* [Install k3d](https://k3d.io/v5.4.7/#installation)
* [Install kubectl](https://kubernetes.io/docs/tasks/tools/)

Check k3d is installed:
```shell=bash
k3d --help
```
Example of output:
```
https://k3d.io/
k3d is a wrapper CLI that helps you to easily create k3s clusters inside docker.
Nodes of a k3d cluster are docker containers running a k3s image.
All Nodes of a k3d cluster are part of the same docker network.

Usage:
  k3d [flags]
  k3d [command]

Available Commands:
  cluster      Manage cluster(s)
  completion   Generate completion scripts for [bash, zsh, fish, powershell | psh]
  config       Work with config file(s)
  help         Help about any command
  image        Handle container images.
  kubeconfig   Manage kubeconfig(s)
  node         Manage node(s)
  registry     Manage registry/registries
  version      Show k3d and default k3s version

Flags:
  -h, --help         help for k3d
      --timestamps   Enable Log timestamps
      --trace        Enable super verbose output (trace logging)
      --verbose      Enable verbose output (debug logging)
      --version      Show k3d and default k3s version

Use "k3d [command] --help" for more information about a command.
```

Create a cluster single node cluster 
```shell=bash
k3d cluster create
```

Create a multi-node cluster without a config file
* 1 Master and 
* 2 Worker nodes.
```shell=bash
k3d cluster create -a 2
```

Create a multi-node cluster using the config file
```shell=bash
kind create cluster --config k3d-config.yaml
```
Example of output:
```bash=shell
➜  k8s-local git:(main) ✗ k3d cluster list  
NAME        SERVERS   AGENTS   LOADBALANCER
k8s-local   1/1       3/3      false
➜  k8s-local git:(main) ✗
```

check the cluster is created
```shell=bash
k3d cluster list
```

Example of outpu:
```shell=
NAME        SERVERS   AGENTS   LOADBALANCER
k8s-local   1/1       3/3      false
```


Accessing the cluster using kubectl
```shell=
kubectl get nodes
```

Example of output:
```shell=
NAME                     STATUS   ROLES                  AGE     VERSION
k3d-k8s-local-server-0   Ready    control-plane,master   9m12s   v1.24.10+k3s1
k3d-k8s-local-agent-1    Ready    <none>                 9m7s    v1.24.10+k3s1
k3d-k8s-local-agent-0    Ready    <none>                 9m7s    v1.24.10+k3s1
k3d-k8s-local-agent-2    Ready    <none>                 9m7s    v1.24.10+k3s1
```

Delete the cluster
```shell=bash
k3d cluster delete <<cluster-name>>
```

The kubectl config file will be updated as cluster gets created or deleted using the k3d in the default location: (~/.kubectl/config).