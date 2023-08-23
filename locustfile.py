import base64, json
import random

from locust import FastHttpUser, task, between

class ZincUser(FastHttpUser):
    org_id = "perf"
    index = "k8s"

    connection_timeout = 600.0
    network_timeout = 600.0
    # wait_time = between(1, 10)

    ## sum by(endpoint) (rate(zo_http_incoming_requests{namespace="ziox-alpha1",organization="default"}[5m]))
    ## sum by(endpoint) (irate(zo_http_incoming_requests{namespace="ziox-alpha1",organization="default"}[5m]))
    ## sum by(endpoint) (increase(zo_http_incoming_requests{namespace="ziox-alpha1",organization="default"}[5m]))
    ## sum by(stream_type) (delta(zo_storage_files{namespace="ziox-alpha1",organization="default"}[5m]))
    ## topk(2, histogram_quantile(0.8, rate(zo_http_response_time_bucket{namespace="ziox-alpha1",organization="default"}[5m])))

    ## --- for prometheus --- ##

    # @task
    # def range_query_rate(self): 
    #     ''' rate '''
    #     self.client.get("/api/v1/query_range?query=sum%20by(endpoint)%20(rate(zo_http_incoming_requests%7Bnamespace%3D%22ziox-alpha1%22%2Corganization%3D%22default%22%7D%5B5m%5D))&start=1682663110&end=1682664910&step=15&db=prometheus", data="", headers={})

    # @task
    # def range_query_irate(self): 
    #     ''' irate '''
    #     self.client.get("/api/v1/query_range?query=sum%20by(endpoint)%20(irate(zo_http_incoming_requests%7Bnamespace%3D%22ziox-alpha1%22%2Corganization%3D%22default%22%7D%5B5m%5D))&start=1682663110&end=1682664910&step=15&db=prometheus", data="", headers={})

    # @task
    # def range_query_increase(self): 
    #     ''' increase '''
    #     self.client.get("/api/v1/query_range?query=sum%20by(endpoint)%20(increase(zo_http_incoming_requests%7Bnamespace%3D%22ziox-alpha1%22%2Corganization%3D%22default%22%7D%5B5m%5D))&start=1682663110&end=1682664910&step=15&db=prometheus", data="", headers={})

    # @task
    # def range_query_delta(self): 
    #     ''' delta '''
    #     self.client.get("/api/v1/query_range?query=sum%20by(stream_type)%20(delta(zo_storage_files%7Bnamespace%3D%22ziox-alpha1%22%2Corganization%3D%22default%22%7D%5B5m%5D))&start=1682663110&end=1682664910&step=15&db=prometheus", data="", headers={})
 
    # @task
    # def range_query_histogram(self): 
    #     ''' histogram '''
    #     self.client.get("/api/v1/query_range?query=topk(2%2C%20histogram_quantile(0.8%2C%20rate(zo_http_response_time_bucket%7Bnamespace%3D%22ziox-alpha1%22%2Corganization%3D%22default%22%7D%5B5m%5D)))&start=1682663110&end=1682664910&step=15&db=prometheus", data="", headers={})


    ## --- for greptimedb --- ##

    # @task
    # def range_query_rate(self): 
    #     ''' rate '''
    #     self.client.get("/v1/promql?query=sum%20by(endpoint)%20(rate(zo_http_incoming_requests%7Bnamespace%3D%22ziox-alpha1%22%2Corganization%3D%22default%22%7D%5B5m%5D))&start=1682663110&end=1682664910&step=15&db=prometheus", data="", headers={})

    # @task
    # def range_query_irate(self): 
    #     ''' irate '''
    #     self.client.get("/v1/promql?query=sum%20by(endpoint)%20(irate(zo_http_incoming_requests%7Bnamespace%3D%22ziox-alpha1%22%2Corganization%3D%22default%22%7D%5B5m%5D))&start=1682663110&end=1682664910&step=15&db=prometheus", data="", headers={})

    # @task
    # def range_query_increase(self): 
    #     ''' increase '''
    #     self.client.get("/v1/promql?query=sum%20by(endpoint)%20(increase(zo_http_incoming_requests%7Bnamespace%3D%22ziox-alpha1%22%2Corganization%3D%22default%22%7D%5B5m%5D))&start=1682663110&end=1682664910&step=15&db=prometheus", data="", headers={})

    # @task
    # def range_query_delta(self): 
    #     ''' delta '''
    #     self.client.get("/v1/promql?query=sum%20by(stream_type)%20(delta(zo_storage_files%7Bnamespace%3D%22ziox-alpha1%22%2Corganization%3D%22default%22%7D%5B5m%5D))&start=1682663110&end=1682664910&step=15&db=prometheus", data="", headers={})

    ## --- for ZincObserve --- ##

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

    # @task
    # def multi_data(self):
    #     '''multi_data does a multi insert in zinc using multi api'''
    #     data = open('data/ziox_multi.json').read()

    #     user = "admin"
    #     password = "Complexpass#123"
    #     bas64encoded_creds = base64.b64encode(bytes(user + ":" + password, "utf-8")).decode("utf-8")

    #     headers = {
    #         'authorization': 'Basic ' + bas64encoded_creds, 
    #         'content-type': 'application/json'
    #     }
    #     self.client.post("/api/" + self.org_id + "/" + self.index + "/_multi", data=data, headers=headers)

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
    #     ''' insert_data does a basic insert in zinc using multi api'''
    #     data =  open('data/ziox_multi.json').read()

    #     user = "root@example.com"
    #     password = "Complexpass#123"
    #     # user = "admin"
    #     # password = "admin"
    #     bas64encoded_creds = base64.b64encode(bytes(user + ":" + password, "utf-8")).decode("utf-8")

    #     headers = {
    #         'authorization': 'Basic ' + bas64encoded_creds, 
    #         'content-type': 'application/json'
    #     }
    #     self.client.post("/api/default/" + self.index + "_multi" + "/_multi", data=data, headers=headers)

    @task
    def insert_json_data(self):
        ''' insert_data does a basic insert in zinc using multi api'''
        data =  open('data/ziox_json_api_100k.json').read()

        user = "root@example.com"
        password = "Complexpass#123"
        # user = "admin"
        # password = "admin"
        bas64encoded_creds = base64.b64encode(bytes(user + ":" + password, "utf-8")).decode("utf-8")

        headers = {
            'authorization': 'Basic ' + bas64encoded_creds, 
            'content-type': 'application/json'
        }
        self.client.post("/api/default/" + self.index + "_json_111" + "/_json", data=data, headers=headers)
