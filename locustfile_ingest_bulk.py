import base64, json
import random

from locust import FastHttpUser, task, between

class ZincUser(FastHttpUser):
 
    connection_timeout = 600.0
    network_timeout = 600.0
    host = "http://localhost:5080/api/default"

    @task
    def insert_ndjson_data(self):
        ''' insert_data does a basic insert in zinc using _bulk api'''
        data = open('data/bulk_100_indexes.ndjson').read()

        user = "root@example.com"
        password = "Complexpass#123"
        bas64encoded_creds = base64.b64encode(bytes(f"{user}:{password}", "utf-8")).decode("utf-8")
        headers = {
            'Authorization': 'Basic ' + bas64encoded_creds,
            'Content-Type': 'application/x-ndjson'
        }

        self.client.post("/_bulk", data=data, headers=headers)
