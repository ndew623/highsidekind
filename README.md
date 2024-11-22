The kind directory contains the configuration file needed to create a kind cluster using `kind create cluster --config kind-config.yaml`.

The examples directory contains the source for docker images, as well as Kubernetes manifests that can be used to deploy those images onto the kind cluster.

All of the Kubernetes manifests are commented with details on the purpose of each line.

# Awetomaton Coder Instructions

## Initial setup
- Once in coder, create a new workspace from the "Develop in Kuberntes" template.
- The name is not important. The default options for CPU, disk size, and memory are fine.
- Open a terminal in the new environment after it builds.
- If you run `kubectl get all` you see should a number of Pods and some `Error from server (Forbidden)` messages.
  - These are resources in a Kubernetes cluster that we DON'T want to use.
- Run this in a terminal to configure your environment with its own test cluster:
```
curl -L https://raw.githubusercontent.com/ndew623/highsidekind/refs/heads/awtmtncoder/setupkind-coder.sh | bash
```
- After that command completes, run `kubectl get all` again. You should see this: `No resources found in coder-ext namespace.`

## Deploying and accessing a website on your test cluster
- If you followed the instructions above, your environment should have a `mnp-k8s-examples/` folder in it.
- In the terminal: `cd mnp-k8s-examples/examples/simple-deployment/image`.
- Run `./build.sh` to both build the image for the website and load it into the test cluster.
- From the `image/` directory `cd ../manifests`.
- You can then run `kubectl apply -f simple-deployment.yaml`
- If you `cat simple-deployment.yaml` you'll see a line near the end of the file that says `nodePort: 30001`. `30001` is the port the deployed website will be accessible on.
- To access port `30001`:
  - Go back to the original coder page (the one with options for VS Code or Terminal).
  - Find the "Open ports" button (upper right).
  - One of the ports in the dropdown menu should be `30001`. Click on it.
- If you see a page displaying the message "simple-deployment works", then you have been successful.

# Kind
The `kind` command line tool can create a Kubernetes cluster using local docker containers for nodes, rather than actual servers in a cluster.

See the kind directory [README.md](kind/README.md) for more details on creating a local kind cluster.

## Loading images into kind
Nodes in any Kubernetes cluster must either be able to pull images named in deployment manifests, or already have those images on the system.

When you build any image in the examples directory, you have two options to make that image available to the cluster:

1. `docker push` those images to a repository that the kind cluster's nodes can `docker pull` from
2. `kind load docker-image <image-name:tag>` to load those images directly into the kind cluster
