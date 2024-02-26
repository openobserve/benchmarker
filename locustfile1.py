import base64, json
import random

from locust import FastHttpUser, task, between

class ZincUser(FastHttpUser):
    stream = "k8s2"

    connection_timeout = 600.0
    network_timeout = 600.0

    @task
    def insert_json_data(self):
        ''' insert_data does a basic insert in zinc using multi api'''
        data =  open('data/k8slog_2.1MB.json').read()

        user = "root@example.com"
        password = "Complexpass#123"
        # user = "admin"
        # password = "admin"
        bas64encoded_creds = base64.b64encode(bytes(user + ":" + password, "utf-8")).decode("utf-8")

        headers = {
            'authorization': 'Basic ' + bas64encoded_creds, 
            'content-type': 'application/json'
        }
        self.client.post("/api/default/" + self.stream + "1/_json", data=data, headers=headers)
        self.client.post("/api/default/" + self.stream + "2/_json", data=data, headers=headers)
        self.client.post("/api/default/" + self.stream + "3/_json", data=data, headers=headers)
        self.client.post("/api/default/" + self.stream + "4/_json", data=data, headers=headers)
    