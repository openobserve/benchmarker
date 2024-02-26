# Artist

Performance benchamrking tool for ZincSearch. It uses [Locust]()

Test requires a k8s cluster.

```shell
kubectl create ns perf1
kubectl apply -f k8s1/leader.yaml
kubectl apply -f k8s1/worker.yaml
```

```shell
kubectl create ns perf2
kubectl apply -f k8s2/leader.yaml
kubectl apply -f k8s2/worker.yaml
```

Worker manifest sets worker count to 10. You can change that based on your needs.

Now let's go to the UI:

```shell
kubectl -n perf1 port-forward svc/locust 8089:8089
kubectl -n perf2 port-forward svc/locust 8090:8089
```

Open the browser and visit http://localhost:8089

Enter the test details (server address and users) that you want to run and proceed. Ideally you want the OpenObserve server to be running in the same cluster.

e.g. inputs:

```pre
server address: http://perf.dev.zinc.svc.cluster.local:4080
Number of users: 100
Spawn rate: 5 
```
