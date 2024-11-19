The kind directory contains the configuration file needed to create a kind cluster using `kind create cluster --config kind-config.yaml`.

The examples directory contains the source for docker images, as well as Kubernetes manifests that can be used to deploy those images onto the kind cluster.

All of the Kubernetes manifest are commented with details on the purpose of each line.

# Kind
The `kind` command line tool can create a Kubernetes cluster using local docker containers for nodes, rather than actual servers in a cluster.

See the kind directory [README.md][kind/README.md] for more details on creating a local kind cluster.

## Loading images into kind
Nodes in any Kubernetes cluster must either be able to pull images named in deployment manifests, or already have those images on the system.

When you build any image in the examples directory, you have two options to make that image available to the cluster:

1. `docker push` those images to a repository that the kind cluster's nodes can `docker pull` from
2. `kind load docker-image <image-name:tag>` to load those images directly into the kind cluster
