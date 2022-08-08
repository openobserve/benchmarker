import base64, json
import random

from locust import FastHttpUser, task

class ZincUser(FastHttpUser):
    index = "perf1"


    # @task
    # def search_basic(self):
    #     ''' search_basic does a basic search for a given query'''
    #     data = json.loads(open('data/query.json').read())
        
    #     headers = {
    #         'authorization': 'Basic YWRtaW4xOlN1cGVybWFuVnNTcGlkZXJtYW4jNzM1',
    #         'content-type': 'application/json'
    #     }
    #     self.client.post("/es/+ self.index + /_search",
    #                      json=data, headers=headers)

    @task
    def insert_bulk_data(self):
        ''' insert_data does a basic insert in zinc using bulk api'''
        data =  open('data/bulk.ndjson').read()

        user = "admin"
        password = "Complexpass#123"
        # user = "admin"
        # password = "admin"
        bas64encoded_creds = base64.b64encode(bytes(user + ":" + password, "utf-8")).decode("utf-8")

        headers = {
            'authorization': 'Basic ' + bas64encoded_creds, 
            'content-type': 'application/json'
        }
        self.client.post("/api/" + self.index + "_bulk" + "/_bulk", data=data, headers=headers)
    
    @task
    def insert_bulkv2_data(self):
        ''' insert_data does a basic insert in zinc using bulkv2 api'''
        data =  json.loads(open('data/bulkv2.json').read())

        user = "admin"
        password = "Complexpass#123"
        # user = "admin"
        # password = "admin"
        bas64encoded_creds = base64.b64encode(bytes(user + ":" + password, "utf-8")).decode("utf-8")

        headers = {
            'authorization': 'Basic ' + bas64encoded_creds, 
            'content-type': 'application/json'
        }

        self.client.post("/api/"+ self.index + "_bulkv2" + "/_bulkv2", json=data, headers=headers)

    @task
    def insert_multi_data(self):
        ''' insert_data does a basic insert in zinc using bulkv2 api'''
        data =  json.loads(open('data/multi.ndjson').read())

        user = "admin"
        password = "Complexpass#123"
        # user = "admin"
        # password = "admin"
        bas64encoded_creds = base64.b64encode(bytes(user + ":" + password, "utf-8")).decode("utf-8")

        headers = {
            'authorization': 'Basic ' + bas64encoded_creds, 
            'content-type': 'application/json'
        }

        self.client.post("/api/"+ self.index + "_multi" + "/_multi", data=data, headers=headers)
