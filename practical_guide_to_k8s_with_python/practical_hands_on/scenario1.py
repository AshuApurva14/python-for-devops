"""

You wrote a Python script that talks to your Kubernetes cluster from your laptop. 
It works great because you have a kubeconfig file in your home directory. 
But once you package that script into a container and run it as a Pod, it fails. 
The Pod does not have your local config file. Hardcoding credentials inside an image is also a massive security risk.

"""

from kubernetes import config, client
import os

def connect_k8s():
    # Check if we are running inside cluster
    if "KUBERNETES_SERVICE_HOST"  in os.environ:
        config.load_incluster_config()
    else:
        # Fallback for local Development

        config.load_kube_config()
    
    v1 = client.CoreV1Api()
    print("Connected to Cluster !")
    return v1

connect_k8s()