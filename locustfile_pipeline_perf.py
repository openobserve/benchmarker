import base64
import json
import random

from locust import FastHttpUser, task, between


class ZincUser(FastHttpUser):

    connection_timeout = 600.0
    network_timeout = 600.0

    @task
    def insert_ndjson_data(self):
        ''' insert_data does a basic insert in zinc using _json api'''
        data = open('data/k8slog_2.1MB.json').read()

        user = "root@example.com"
        password = "ac0dcdf1c5a1183bd78a9bdb67e18406"
        bas64encoded_creds = base64.b64encode(
            bytes(f"{user}:{password}", "utf-8")).decode("utf-8")
        headers = {
            'Authorization': 'Basic ' + bas64encoded_creds,
            'Content-Type': 'application/json'
        }

        self.client.post(
            "/api/default/pipeline_perf/_json", data=data, headers=headers)
