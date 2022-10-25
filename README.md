# Artist

Performance benchamrking tool for ZincSearch. It uses [Locust]()

Test requires a k8s cluster.

```shell
kubectl create ns perf
kubectl apply -f k8s/leader.yaml
kubectl apply -f k8s/worker.yaml
```

Worker manifest sets worker count to 10. You can change that based on your needs.

Now let's go to the UI:

```shell
kubectl -n perf port-forward svc/locust 8089:8089
```

Open the browser and visit http://localhost:8089

Enter the test details (server address and users) that you want to run and proceed. Ideally you want the zinc server to be running in the same cluster.

e.g. inputs:

```pre
server address: http://perf.dev.zinc.svc.cluster.local:4080
Number of users: 100
Spawn rate: 5 
```
