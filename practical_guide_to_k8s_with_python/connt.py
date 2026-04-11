from kubernetes import client, config

# This is will find config and set the context
config.load_kube_config(context="dev-cluster")

v1 = client.CoreV1Api()

print("Listing pods:")

ret = v1.list_pod_for_all_namespaces(watch=False)

for i in ret.items:
    priint(f"{i.status.pod_ip}- {i.metadata.name}")