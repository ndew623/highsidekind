Unlike some of the other examples there are no separate images and manifests directory for this one.

The job will just use a simple alpine base image (anything with /bin/sh in it should work).

The command for the image is set to be ``echo "The job ran at " `date` "."``.

Run `kubectl create -f cron-job.yaml` to create the Job.

The CronJob is configured to run every two minutes.

After two minutes the Job should have created a Pod. You can find it by running `kubectl get pod`.

If one of the Pod's statuses is "Completed", copy the pod name into this command: `kubectl logs <pod-name>`.

You should see `The job ran at <timestamp>.` in the logs.
