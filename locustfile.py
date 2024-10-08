import base64
import random
import time
import json
from locust import FastHttpUser, task

# Convert current time to epoch microseconds
current_time_microseconds = int(time.time() * 1e6)

# Subtract 1 week in microseconds
one_week_microseconds = 7 * 24 * 60 * 60 * 1_000_000
start_time = current_time_microseconds - one_week_microseconds
end_time = current_time_microseconds

# Load queries from JSON file
with open('data/queries.json', 'r') as f:
    queries = json.load(f)["queries"]

class ZincUser(FastHttpUser):
    connection_timeout = 600.0
    network_timeout = 600.0
    host = "http://zo1-openobserve-router.perfb.svc.cluster.local:5080/api/default"

    user = "root@example.com"
    password = "Complexpass@800"
    bas64encoded_creds = base64.b64encode(bytes(f"{user}:{password}", "utf-8")).decode("utf-8")
    headers = {
        'Authorization': 'Basic ' + bas64encoded_creds,
        'Content-Type': 'application/json'
    }

    @task
    def run_queries(self):
        for query in queries:
            # Replace placeholders with actual times
            # query['start_time'] = start_time
            # query['end_time'] = end_time
            
            # user fixed start and end time
            # 2024-09-26T00:00:00Z - 2024-09-26T00:05:00Z
            query['start_time'] = 1727308800000000
            query['end_time'] = 1727309100000000
            
            self.client.post("/_search?type=logs&use_cache=true", name=f"/query/{query['name']}", json={"query": query}, headers=self.headers)
            break
