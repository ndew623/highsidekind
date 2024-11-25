In this example kustomize is used to change the number of replicas in a deployment.

There is no image/ directory, it uses the same image as the multiple-replica-deployment example.

If you apply the deployment in `manifests/base/deploy.yaml` directly you will only get one replica.

If you apply the deployment in `manifests/envs/prod/` using `kubectl kustomize | kubectl apply -f -` you will get 7 replicas.

You can see that there are multiple replicas by repeatedly refreshing the page and seeing the slightly different startup times each time you get a different Pod.

Use port 30004.

----------
Tip: You can quickly cleanup the created resources using `kubectl kustomize | kubectl delete -f -`.
