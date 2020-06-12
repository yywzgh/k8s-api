from kubernetes import client, config


def list_svc():
    conn = client.CoreV1Api()
    for pod in conn.list_namespaced_pod(namespace="default").items:
        print(pod.metadata.name)


config.load_kube_config("config.yaml")

list_svc()