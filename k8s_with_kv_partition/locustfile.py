import base64
from locust import HttpUser, task, between

class MonitorUser(HttpUser):
    wait_time = between(1, 3)  # Wait time between requests (1-3 sec)

    user = "ashish@openobserve.ai"
    password = "aa"
    bas64encoded_creds = base64.b64encode(bytes(f"{user}:{password}", "utf-8")).decode("utf-8")
    headers = {
        'Authorization': 'Basic ' + bas64encoded_creds,
        'Content-Type': 'application/json'
    }

    @task
    def test_bulk_endpoint(self):
        """Read NDJSON file and send bulk request to Elasticsearch"""
        with open("bulk.ndjson", "r") as file:
            ndjson_data = file.read()  # Read entire NDJSON file as a single string
        
        # Send the bulk request to Elasticsearch
     
        self.client.post("/_bulk", data=ndjson_data, headers=self.headers)