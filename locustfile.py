import base64, json
import random

from locust import FastHttpUser, task, between

class ZincUser(FastHttpUser):
    index = "perf3"

    connection_timeout = 600.0
    network_timeout = 600.0
    # wait_time = between(1, 10)

    # @task
    # def search_basic(self):
    #     ''' search_basic does a basic search for a given query'''
    #     data = json.loads(open('data/query_ziox_sql.json').read())

    #     user = "admin"
    #     password = "Complexpass#123"
    #     bas64encoded_creds = base64.b64encode(bytes(user + ":" + password, "utf-8")).decode("utf-8")

    #     headers = {
    #         'authorization': 'Basic ' + bas64encoded_creds, 
    #         'content-type': 'application/json'
    #     }
    #     self.client.post("/api/single/_search?sql", json=data, headers=headers)

    # @task
    # def search_basic_match(self):
    #     ''' search_basic does a basic search for a given query'''
    #     data = json.loads(open('data/query_ziox_sql_match.json').read())

    #     user = "admin"
    #     password = "Complexpass#123"
    #     bas64encoded_creds = base64.b64encode(bytes(user + ":" + password, "utf-8")).decode("utf-8")

    #     headers = {
    #         'authorization': 'Basic ' + bas64encoded_creds, 
    #         'content-type': 'application/json'
    #     }
    #     self.client.post("/api/single/_search?sql_match", json=data, headers=headers)

    # @task
    # def search_basic_match_all(self):
    #     ''' search_basic does a basic search for a given query'''
    #     data = json.loads(open('data/query_ziox_sql_match_all.json').read())

    #     user = "admin"
    #     password = "Complexpass#123"
    #     bas64encoded_creds = base64.b64encode(bytes(user + ":" + password, "utf-8")).decode("utf-8")

    #     headers = {
    #         'authorization': 'Basic ' + bas64encoded_creds, 
    #         'content-type': 'application/json'
    #     }
    #     self.client.post("/api/single/_search?sql_match_all", json=data, headers=headers)

    # @task
    # def search_basic_match_all_case(self):
    #     ''' search_basic does a basic search for a given query'''
    #     data = json.loads(open('data/query_ziox_sql_match_all_case.json').read())

    #     user = "admin"
    #     password = "Complexpass#123"
    #     bas64encoded_creds = base64.b64encode(bytes(user + ":" + password, "utf-8")).decode("utf-8")

    #     headers = {
    #         'authorization': 'Basic ' + bas64encoded_creds, 
    #         'content-type': 'application/json'
    #     }
    #     self.client.post("/api/single/_search?sql_match_all_case", json=data, headers=headers)

    # @task
    # def search_basic_aggs_term(self):
    #     ''' search_basic does a basic search for a given query'''
    #     data = json.loads(open('data/query_ziox_sql_aggs_term.json').read())

    #     user = "admin"
    #     password = "Complexpass#123"
    #     bas64encoded_creds = base64.b64encode(bytes(user + ":" + password, "utf-8")).decode("utf-8")

    #     headers = {
    #         'authorization': 'Basic ' + bas64encoded_creds, 
    #         'content-type': 'application/json'
    #     }
    #     self.client.post("/api/single/_search?sql_aggs_term", json=data, headers=headers)

    # @task
    # def search_basic_aggs_histogram(self):
    #     ''' search_basic does a basic search for a given query'''
    #     data = json.loads(open('data/query_ziox_sql_aggs_histogram.json').read())

    #     user = "admin"
    #     password = "Complexpass#123"
    #     bas64encoded_creds = base64.b64encode(bytes(user + ":" + password, "utf-8")).decode("utf-8")

    #     headers = {
    #         'authorization': 'Basic ' + bas64encoded_creds, 
    #         'content-type': 'application/json'
    #     }
    #     self.client.post("/api/single/_search?sql_aggs_histogram", json=data, headers=headers)

    @task
    def multi_data(self):
        '''multi_data does a multi insert in zinc using multi api'''
        data = open('data/ziox_multi.json').read()

        user = "admin"
        password = "Complexpass#123"
        bas64encoded_creds = base64.b64encode(bytes(user + ":" + password, "utf-8")).decode("utf-8")

        headers = {
            'authorization': 'Basic ' + bas64encoded_creds, 
            'content-type': 'application/json'
        }
        self.client.post("/api/perf/k8s/_multi", data=data, headers=headers)

    # @task
    # def insert_bulk_data(self):
    #     ''' insert_data does a basic insert in zinc using bulk api'''
    #     data =  open('data/bulk.ndjson').read()

    #     user = "admin"
    #     password = "Complexpass#123"
    #     # user = "admin"
    #     # password = "admin"
    #     bas64encoded_creds = base64.b64encode(bytes(user + ":" + password, "utf-8")).decode("utf-8")

    #     headers = {
    #         'authorization': 'Basic ' + bas64encoded_creds, 
    #         'content-type': 'application/json'
    #     }
    #     # self.client.post("/api/" + self.index + "_bulk" + "/_bulk", data=data, headers=headers)
    #     self.client.post("/api/_bulk", data=data, headers=headers)
    
    # @task
    # def insert_bulkv2_data(self):
    #     ''' insert_data does a basic insert in zinc using bulkv2 api'''
    #     data =  json.loads(open('data/bulkv2.json').read())

    #     user = "admin"
    #     password = "Complexpass#123"
    #     # user = "admin"
    #     # password = "admin"
    #     bas64encoded_creds = base64.b64encode(bytes(user + ":" + password, "utf-8")).decode("utf-8")

    #     headers = {
    #         'authorization': 'Basic ' + bas64encoded_creds, 
    #         'content-type': 'application/json'
    #     }

    #     self.client.post("/api/"+ self.index + "_bulkv2" + "/_bulkv2", json=data, headers=headers)

    # @task
    # def insert_multi_data(self):
    #     ''' insert_data does a basic insert in zinc using bulk api'''
    #     data =  open('data/multi.ndjson').read()

    #     user = "admin"
    #     password = "Complexpass#123"
    #     # user = "admin"
    #     # password = "admin"
    #     bas64encoded_creds = base64.b64encode(bytes(user + ":" + password, "utf-8")).decode("utf-8")

    #     headers = {
    #         'authorization': 'Basic ' + bas64encoded_creds, 
    #         'content-type': 'application/json'
    #     }
    #     self.client.post("/api/" + self.index + "_multi" + "/_multi", data=data, headers=headers)
