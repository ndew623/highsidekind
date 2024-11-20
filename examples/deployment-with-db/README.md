The images directory contains source code for three images.
- The first image is a postgres database.
- The second image is a backend service written in python. It provides an API for accessing the database.
- The third image is a website that uses the backend api.

To build the docker images, run `./build.sh` in their respective directories. You will need base images for python, postgres, and nginx. You may need to edit the Dockerfiles to build from whatever base images you have.

The manifests directory contains YAML to deploy these components in a kind cluster.

Upon success, you should be able to navigate to the endpoint defined in the Service manifest with your web browser.
