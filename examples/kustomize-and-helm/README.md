This example shows using kustomize with a helm chart.

The helm chart is under `base/charts-dir/`, and creates 3 nginx replicas.

`base/kustomization.yaml` points to the helm chart dir, as well as a new values.yaml file that overrides the number of nginx replicas to be 4 instead of 3.

In `envs/dev/`, the kustomization file and patch file add a `environment: dev` label to the deployment. The number of replicas is left at 4.

In `envs/prod/`, the kustomization file and patch file add a `environment: prod` label to the deployment. They also change the number of replicas to 10.

---

To test:
1. `cd` into either `envs/dev/` or `envs/prod/`
2. run `kubectl kustomize --enable-helm` and inspect the output.
