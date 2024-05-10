import os
import requests
import json
from requests.auth import HTTPBasicAuth


def send_batch_to_endpoint(file_name, batch_data, counter):
    """
    Send a batch of data to the HTTP endpoint.
    
    :param batch_data: List of dictionaries representing the rows to send
    """

    
    ENDPOINT_URL="http://localhost:5080/api/default/" + file_name + "/_json"
    USERNAME="root@example.com"
    PASSWORD="Complexpass#123"
    CHUNK_SIZE=30

    try:
        # Include the auth parameter in the post request
        response = requests.post(
            ENDPOINT_URL,
            json=batch_data,
            auth=HTTPBasicAuth(USERNAME, PASSWORD)
        )
        response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
        print(f"Batch sent successfully for counter: {counter} . Response status code: {response.status_code}")
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_name = "1000"

    # Read the data from the file
    with open('50_records_' + file_name + '_fields.json') as f:
        data = json.load(f)

    
    # Send the data to the endpoint 100 times
    for i in range(100): 
      send_batch_to_endpoint(file_name, data, i)