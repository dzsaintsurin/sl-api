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
> `k3d --help`
```shell=bash
k3d --help

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
> `k3d cluster create my-single-node-cluster`
```shell=bash
k3d cluster create my-single-node-cluster
INFO[0000] Prep: Network
INFO[0000] Created network 'k3d-my-single-node-cluster'
INFO[0000] Created image volume k3d-my-single-node-cluster-images
INFO[0000] Starting new tools node...
....
INFO[0016] Injecting records for hostAliases (incl. host.k3d.internal) and for 3 network members into CoreDNS configmap...
INFO[0018] Cluster 'my-single-node-cluster' created successfully!
INFO[0018] You can now use it like this:
kubectl cluster-info
```

Cluster Info
> `kubectl cluster-info`
```shell=
➜  k8s-local git:(main) ✗ kubectl cluster-info
Kubernetes control plane is running at https://0.0.0.0:39329
CoreDNS is running at https://0.0.0.0:39329/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
Metrics-server is running at https://0.0.0.0:39329/api/v1/namespaces/kube-system/services/https:metrics-server:https/proxy
```

Check cluster info via k3d command
> `k3d cluster ls`
```shell=
➜  k8s-local git:(main) ✗ k3d cluster ls
NAME                     SERVERS   AGENTS   LOADBALANCER
my-single-node-cluster   1/1       0/0      true
➜  k8s-local git:(main) ✗
```
Create a multi-node cluster without a config file
* 1 Master and 
* 2 Worker nodes.
> `k3d cluster create -a 2 my-2-node-k8s-cluster`
```shell=bash
➜  k8s-local git:(main) ✗ k3d cluster create -a 2 my-2-node-k8s-cluster
# Output below:
INFO[0000] Prep: Network
INFO[0000] Created network 'k3d-my-2-node-k8s-cluster'
INFO[0000] Created image volume k3d-my-2-node-k8s-cluster-images
INFO[0000] Starting new tools node...
INFO[0000] Starting Node 'k3d-my-2-node-k8s-cluster-tools'
INFO[0001] Creating node 'k3d-my-2-node-k8s-cluster-server-0'
... More lines
INFO[0012] Starting Node 'k3d-my-2-node-k8s-cluster-serverlb'
INFO[0018] Injecting records for hostAliases (incl. host.k3d.internal) and for 5 network members into CoreDNS configmap...
INFO[0020] Cluster 'my-2-node-k8s-cluster' created successfully!
INFO[0020] You can now use it like this:
kubectl cluster-info
```

Verify the k8s clusters have been created:
> `k3d cluster ls`
```shell=
➜  k8s-local git:(main) ✗ k3d cluster ls
# Output below:
NAME                     SERVERS   AGENTS   LOADBALANCER
my-2-node-k8s-cluster    1/1       2/2      true
my-single-node-cluster   1/1       0/0      true
```

Create a multi-node cluster using a config file.
> `k3d cluster create -c k3d-config.yaml`
```shell=bash
k3d cluster create -c k3d-config.yaml
INFO[0000] Using config file k3d-config.yaml (k3d.io/v1alpha4#simple)
INFO[0000] Prep: Network
INFO[0000] Created network 'k3d-k8s-local'
INFO[0000] Created image volume k3d-k8s-local-images
... A few more lines
INFO[0015] Cluster 'k8s-local' created successfully!
INFO[0015] You can now use it like this:
kubectl cluster-info
```

Verify all 3 created clusters:
> `k3d cluster list `
```shell=
➜  k8s-local git:(main) ✗ k3d cluster ls
NAME                     SERVERS   AGENTS   LOADBALANCER
k8s-local                1/1       3/3      false
my-2-node-k8s-cluster    1/1       2/2      true
my-single-node-cluster   1/1       0/0      true
```

Delete a cluster by name (Example: my-2-node-k8s-cluster)
> `k3d cluster delete my-2-node-k8s-cluster`
```shell=bash
➜  k8s-local git:(main) ✗ k3d cluster delete my-2-node-k8s-cluster
INFO[0000] Deleting cluster 'my-2-node-k8s-cluster'
INFO[0004] Deleting cluster network 'k3d-my-2-node-k8s-cluster'
INFO[0004] Deleting 1 attached volumes...
INFO[0004] Removing cluster details from default kubeconfig...
INFO[0004] Removing standalone kubeconfig file (if there is one)...
INFO[0004] Successfully deleted cluster my-2-node-k8s-cluster!
➜  k8s-local git:(main) ✗
```
Verify cluster name 'my-2-node-k8s-cluster' is gone:
> `k3d cluster ls`
```shell=
k3d cluster ls
NAME                     SERVERS   AGENTS   LOADBALANCER
k8s-local                1/1       3/3      false
my-single-node-cluster   1/1       0/0      true
➜  k8s-local git:(main) ✗
```
Delete Every cluster created using k3d all at once.
> `k3d cluster delete -a`
```shell=
k3d cluster delete -a
INFO[0000] Deleting all clusters...
INFO[0000] Deleting cluster 'k8s-local'
INFO[0004] Deleting cluster network 'k3d-k8s-local'
INFO[0004] Deleting 1 attached volumes...
INFO[0004] Removing cluster details from default kubeconfig...
INFO[0004] Removing standalone kubeconfig file (if there is one)...
INFO[0004] Successfully deleted cluster k8s-local!
INFO[0004] Deleting cluster 'my-single-node-cluster'
INFO[0006] Deleting cluster network 'k3d-my-single-node-cluster'
INFO[0006] Deleting 1 attached volumes...
INFO[0006] Removing cluster details from default kubeconfig...
INFO[0006] Removing standalone kubeconfig file (if there is one)...
INFO[0006] Successfully deleted cluster my-single-node-cluster!
```

The kubectl config file will be updated as cluster gets created or deleted using the k3d in the default location: (~/.kubectl/config).

### More on k3d can be found [here](https://k3d.io/v5.0.1/) on their website. K3d is k3s on Docker.