The image directory contains the Dockerfile for a simple static website hosted by an nginx container.

To build the docker container, run `./build.sh` in the image directory. the system will need an nginx image.

The manifests directory contains a Deployment and Service for use in a kind Kubernetes cluster.

Upon success, you should be able to navigate to the endpoint defined in the Service manifest with your web browser and see a blue rectangle containing the message "simple-deployment works".
