set -euxo pipefail

# For AMD64 / x86_64
[ x86_64 = x86_64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.25.0/kind-linux-amd64
# For ARM64
[ x86_64 = aarch64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.25.0/kind-linux-arm64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind

git clone https://github.com/ndew623/highsidekind.git

mv highsidekind mnp-k8s-examples

kind create cluster --config=./mnp-k8s-examples/kind/kind-config.yaml

kubectl cluster-info --context kind-kind

kubectl create ns coder-ext
