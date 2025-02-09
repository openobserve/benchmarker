import base64, json
import random

from locust import FastHttpUser, task, between

class ZincUser(FastHttpUser):
 
    connection_timeout = 600.0
    network_timeout = 600.0
    host = "http://simd-test-openobserve-router.simdtest.svc.cluster.local:5080/api/default"

    
    @task
    def insert_ndjson_data(self):
        ''' insert_data does a basic insert in zinc using _bulk api'''
        data = open('data/ziox_multi_600.json').read()

        user = "admin@example.com"
        password = "Complexpass@700"

        # user = "admin"
        # password = "admin"
        bas64encoded_creds = base64.b64encode(bytes(user + ":" + password, "utf-8")).decode("utf-8")

        headers = {
            'authorization': 'Basic ' + bas64encoded_creds, 
            'content-type': 'application/json'
        }
        self.client.post("/ingest_locust/_multi", data=data, headers=headers)
