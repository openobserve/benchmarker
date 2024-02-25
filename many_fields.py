import json

# Initial data provided as a dictionary
data =     {
        "kubernetes.annotations.kubectl.kubernetes.io/default-container": "prometheus",
        "kubernetes.annotations.kubernetes.io/psp": "eks.privileged",
        "kubernetes.container_hash": "quay.io/prometheus/prometheus@sha256:4748e26f9369ee7270a7cd3fb9385c1adb441c05792ce2bce2f6dd622fd91d38",
        "kubernetes.container_image": "quay.io/prometheus/prometheus:v2.39.1",
        "kubernetes.container_name": "prometheus",
        "kubernetes.docker_id": "563f8f40062cd0188c11f39e89d47e6eacddb5624a8a93b39f77ec53b5c38bf5",
        "kubernetes.host": "ip-10-2-50-35.us-east-2.compute.internal",
        "kubernetes.labels.app.kubernetes.io/component": "prometheus",
        "kubernetes.labels.app.kubernetes.io/instance": "k8s",
        "kubernetes.labels.app.kubernetes.io/managed-by": "prometheus-operator",
        "kubernetes.labels.app.kubernetes.io/name": "prometheus",
        "kubernetes.labels.app.kubernetes.io/part-of": "kube-prometheus",
        "kubernetes.labels.app.kubernetes.io/version": "2.39.1",
        "kubernetes.labels.controller-revision-hash": "prometheus-k8s-5857d9766c",
        "kubernetes.labels.operator.prometheus.io/name": "k8s",
        "kubernetes.labels.operator.prometheus.io/shard": "0",
        "kubernetes.labels.prometheus": "k8s",
        "kubernetes.labels.statefulset.kubernetes.io/pod-name": "prometheus-k8s-1",
        "kubernetes.namespace_name": "monitoring",
        "kubernetes.pod_id": "ebdc171d-c891-495f-b4d6-e24711b70e64",
        "kubernetes.pod_name": "prometheus-k8s-1",
        "log": "ts=2022-12-27T14:09:59.212Z caller=klog.go:108 level=warn component=k8s_client_runtime func=Warningf msg=\"pkg/mod/k8s.io/client-go@v0.25.1/tools/cache/reflector.go:169: failed to list *v1.Pod: pods is forbidden: User \\\"system:serviceaccount:monitoring:prometheus-k8s\\\" cannot list resource \\\"pods\\\" in API group \\\"\\\" at the cluster scope\"",
        "stream": "stderr"
    }

# Calculate how many dummy fields we need to add
fields_to_add = 1000 - len(data)

# Add dummy fields to reach 1000 fields
for i in range(fields_to_add):
    data[f"dummy_field_{i+1}"] = f"dummy_value_{i+1}"

# Now create an array of 1000 objects with the new structure
data_array = [data.copy() for _ in range(50)]

# If you need to output this to a JSON file:
with open('data.json', 'w') as f:
    json.dump(data_array, f, indent=4)

# If you need to keep it in the script, you can use it directly
# print(json.dumps(data_array, indent=4))
