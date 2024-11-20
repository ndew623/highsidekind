This deployment is for a simple website.

When you access the website, you should see a message that says when the Pod hosting the website started.

Since we have 4 replicas in this example, there will be 4 Pods.

Not all of the Pods will have started at the exact same time.

If you repeatedly hard-refresh the page, you should see 4 different timestamps (probably separated by a second or less).

This is because the Service will automatically load-balance between the 4 Pods.

The deployment should be accessible on port 30002 (the specified `nodePort` in the manifest) on the machine running the cluster.