# Kustomize deployment.
This deployment uses kustomize.
```sh=
kustomize build k8s-local
```
### Directory Structure
```
sl-api-k8s
├── README.md
├── base
│   ├── deploy.yml
│   ├── kustomization.yml
│   ├── namespace.yml
│   └── service.yml
├── k8s-local
│   └── kustomization.yml
└── nohup.out

````

This k8s deployment has 4 components.
* Namespace (Namespace name: sl-api)
* Deployment with 3 pod replicas (Deployment name: deploy-sl-api )
* Service of type Loadbalancer: (Service Name: svc-sl-api)
```sh=
NAME                        STATUS   AGE
namespace/default           Active   12h
namespace/kube-system       Active   12h
namespace/kube-public       Active   12h
namespace/kube-node-lease   Active   12h
namespace/sl-api            Active   9h

NAME                            READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/deploy-sl-api   3/3     3            3           9h

NAME                 TYPE           CLUSTER-IP    EXTERNAL-IP   PORT(S)          AGE
service/svc-sl-api   LoadBalancer   10.43.71.42   <pending>     8080:32659/TCP   9h
```

This deployment use [kustomize](https://kustomize.io/)


# 
## [Back to Main Readme](../README.md)