import json
import random
import string
from requests.auth import HTTPBasicAuth
import requests
import time

# Function to generate a random string
def random_string(length=10):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

# Function to generate a single JSON record with random keys and values
def generate_random_json():
    num_keys = random.randint(5, 10)
    return {random_string(): random_string() for _ in range(num_keys)}

# Function to generate an array of JSON records
def generate_json_records(num_records):
    return [generate_random_json() for _ in range(num_records)]

# HTTP endpoint and basic auth credentials
url = 'http://localhost:5080/api/default/random2/_json'
username = 'root@example.com'
password = 'Complexpass#123'

# Loop 500 times
for i in range(5):
    start_time = time.time()
    # Generate 1000 JSON records
    json_records = generate_json_records(100)
    
    # Convert the records to a JSON string
    json_data = json.dumps(json_records)

    # Send the data to the HTTP endpoint
    response = requests.post(
        url,
        data=json_data,
        auth=HTTPBasicAuth(username, password),
        headers={'Content-Type': 'application/json'}
    )
    
    # Check if the request was successful
    if response.status_code == 200:
        print(f'Batch {i+1}/500 sent successfully.')
    else:
        print(f'Error sending batch {i+1}/500: HTTP {response.status_code} - {response.reason}')

    # calculate total time spent sending data in this loop
    end_time = time.time()
    total_time = end_time - start_time
    print(f'Time spent sending data in loop {i}: {total_time} seconds')


