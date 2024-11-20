Unlike some of the other examples there are no separate images and manifests directory for this one.

The job will just use a simple alpine base image (anything with sh or bash in it will work).

The command for the image is set to be `echo "The job ran."`.

Run `kubectl create -f simple-job.yaml` to create the Job.

After the Job is created you should be able to find the Pod it creates by running `kubectl get pod`.

If the Pod's status is "Completed", copy the pod name into this command: `kubectl logs <pod-name>`.

You should see `The job ran.` in the logs.

To run the job again, you have to delete it and re-`kubectl create` or `kubectl apply` it.