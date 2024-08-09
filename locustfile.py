import base64, json
import random

from locust import FastHttpUser, task, tag, between

import json
import random

class ZincUser(FastHttpUser):
    # wait_time = between(1, 5)  # Adjust as necessary
    connection_timeout = 600.0
    network_timeout = 600.0
    host = "http://simdtest-openobserve-router.simdtest.svc.cluster.local:5080/api/default"

    @task
    def query_basic_select(self):
        data = {
            "query": {
                "sql": "select * from default",
                "from": 0,
                "size": 10,
                "start_time": 1719754035717000,
                "end_time": 1722432435717000
            }
        }

        user = "root@example.com"
        password = "Complexpass#123"
        bas64encoded_creds = base64.b64encode(bytes(f"{user}:{password}", "utf-8")).decode("utf-8")

        headers = {
            'Authorization': 'Basic ' + bas64encoded_creds,
            'Content-Type': 'application/json'
        }

        self.client.post("/_search?type=logs&use_cache=false", name="/query/base-select", json=data, headers=headers)


    @task
    def query_match_all(self):
        data = {
            "query": {
                "sql": "select * from default where match_all('fluent')",
                "from": 0,
                "size": 10,
                "start_time": 1719754035717000,
                "end_time": 1722432435717000
            }
        }

        user = "root@example.com"
        password = "Complexpass#123"
        bas64encoded_creds = base64.b64encode(bytes(f"{user}:{password}", "utf-8")).decode("utf-8")

        headers = {
            'Authorization': 'Basic ' + bas64encoded_creds,
            'Content-Type': 'application/json'
        }

        self.client.post("/_search?type=logs&use_cache=false", name="/query/match_all", json=data, headers=headers)


    @task
    def query_histogram(self):
        data = {
            "query": {
                "sql": "select histogram(_timestamp, '10 second') AS zo_sql_key, count(*) AS zo_sql_num from default GROUP BY zo_sql_key ORDER BY zo_sql_key",
                "from": 0,
                "size": 10,
                "sql_mode": "full",
                "start_time": 1719754035717000,
                "end_time": 1722432435717000
            }
        }

        user = "root@example.com"
        password = "Complexpass#123"
        bas64encoded_creds = base64.b64encode(bytes(f"{user}:{password}", "utf-8")).decode("utf-8")

        headers = {
            'Authorization': 'Basic ' + bas64encoded_creds,
            'Content-Type': 'application/json'
        }

        self.client.post("/_search?type=logs&use_cache=false", name="/query/histogram", json=data, headers=headers)

# locust -f locustfile.py
# localhost::8089
