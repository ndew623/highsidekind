A minimal example of a helm chart.

- `nginx/Chart.yaml`
  - contains metadata about the chart, like name and version
- `nginx/templates/`
  - contains the k8s manifests that make up the chart
  - manifests use golang templating to specify how a values.yaml file can modify the chart
- `nginx/values.yaml`
  - default values for the chart
  - used to complete the templates in the templates folder

---

To test do either:
- `helm install my-nginx nginx/` to deploy to the cluster
  - `helm list` to see it is installed
  - `kubectl get pod` to see 3 nginx pods
  - `helm uninstall my-nginx` to uninstall
- `helm template nginx/` to see the "inflated" helm chart without applying to the cluster
  - an "inflated" helm chart is the result of combining a values.yaml with `templates/`
  - you should see `replicas: 3` in the output
