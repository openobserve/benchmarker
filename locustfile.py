import base64, json
import random

from locust import FastHttpUser, task, between

class ZincUser(FastHttpUser):
 
    connection_timeout = 600.0
    network_timeout = 600.0
    host = "http://zo1-openobserve-router.perfb.svc.cluster.local:5080/api/default"
    stream = "default"

    @task
    def insert_ndjson_data(self):
        ''' insert_data does a basic insert in zinc using _bulk api'''
        data = open('data/ziox_multi_600.json').read()

        user = "root@example.com"
        password = "Complexpass@800"
        bas64encoded_creds = base64.b64encode(bytes(f"{user}:{password}", "utf-8")).decode("utf-8")
        headers = {
            'Authorization': 'Basic ' + bas64encoded_creds,
            'Content-Type': 'application/json'
        }

        self.client.post("/" + self.stream + "/_multi", data=data, headers=headers)
