## Connecting Python to Your Cluster

You want to automate your cluster, but your script does not know where it lives or how to log in. Manually hardcoding IP addresses and tokens into your code is a security nightmare. It also breaks the moment you switch from a development cluster to a production one.

The kubernetes Python client uses config.load_kube_config() to solve this. This function basically mimics how kubectl works by reading your local configuration files. It handles SSL certificate verification and token refreshes for you automatically.

    •
    It looks for the $KUBECONFIG environment variable first.
    •
    It defaults to the ~/.kube/config file if no variable is set.
    •
    It lets you target specific clusters by name using the context argument.

First, install the official library: pip install kubernetes