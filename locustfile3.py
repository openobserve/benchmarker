import base64, json
import random

from locust import FastHttpUser, task, between

# Function to generate a random value of a specified type
def generate_random_value(value_type):
    if value_type == "int":
        return random.randint(1, 100)
    elif value_type == "float":
        return random.uniform(1.0, 100.0)
    elif value_type == "string":
        return f"random_string_{random.randint(1, 100)}"
    elif value_type == "bool":
        return random.choice([True, False])
    elif value_type == "list":
        return [random.randint(1, 10) for _ in range(3)]
    elif value_type == "dict":
        return {"key": random.randint(1, 10)}
    # Removed the function type to ensure JSON serializability
    else:
        return None

# Function to add 10 specific attributes with changing values and types
def add_specific_attributes(data_dict):
    data_types = ["int", "float", "string", "bool", "list", "dict", "function"]
    for i in range(1, 20):
        value_type = random.choice(data_types)
        data_dict[f"ts_event_user_extra_authentication_kubernetes_io_attr{i}"] = generate_random_value(value_type)

# Function to add 10 random attributes to a given dictionary
def add_random_attributes(data_dict):
    for _ in range(1, random.randint(1, 100)):
        key = f"random_attr_{random.randint(1, 6000)}"
        value = generate_random_value(random.choice(["int", "float", "string", "bool", "list", "dict"]))
        data_dict[key] = value

class O2User(FastHttpUser):
    wait_time = between(1, 2.5)

    f1 = 'data/many_fields/50_records_1000_fields_2.2MB.json'
    f2 = 'data/k8slog.json'
    f3 = 'data/k8slog.ndjson'

    def load_f3(self) -> None:
        with open(self.f3, 'r') as file:
            modified_data = []
            for index, line in enumerate(file):
                row = json.loads(line)  # Convert each line to a dictionary
                
                # Apply modifications
                if index % 2 == 0:  # Even-numbered rows (0-indexed)
                    add_specific_attributes(row)
                if random.random() < 0.5:  # Randomly add attributes to about 50% of rows
                    add_random_attributes(row)

                # Convert the dictionary back to a JSON string and add it to the list
                modified_data.append(json.dumps(row))
            self.data['f3'] = "\n".join(modified_data)

    def on_start(self) -> None:
        self.data = {}
        self.json_ep = '/api/default/default/_json'
        self.bulk_ep = '/api/default/_bulk'
        with open(self.f1) as f:
            self.data['f1'] = json.load(f)
        
        with open(self.f2) as f:
            self.data['f2'] = json.load(f)

        self.load_f3()

    @task
    def json_log_ingestion_f1(self):
        user = "root@example.com"
        password = "Complexpass#123"
        bas64encoded_creds = base64.b64encode(bytes(user + ":" + password, "utf-8")).decode("utf-8")
        headers = {
            'authorization': 'Basic ' + bas64encoded_creds, 
            'content-type': 'application/json',
        }
        self.client.post(self.json_ep, json=self.data['f1'], headers=headers)

    @task
    def json_log_ingestion_f2(self):
        user = "root@example.com"
        password = "Complexpass#123"
        bas64encoded_creds = base64.b64encode(bytes(user + ":" + password, "utf-8")).decode("utf-8")
        headers = {
            'authorization': 'Basic ' + bas64encoded_creds, 
            'content-type': 'application/json'
        }
        self.client.post(self.json_ep, json=self.data['f2'], headers=headers)

    @task
    def insert_ndjson_data(self):
        user = "root@example.com"
        password = "Complexpass#123"
        bas64encoded_creds = base64.b64encode(bytes(user + ":" + password, "utf-8")).decode("utf-8")
        headers = {
            'authorization': 'Basic ' + bas64encoded_creds, 
            'Content-Type': 'application/x-ndjson'
        }
        self.client.post(self.bulk_ep, data=self.data['f3'], headers=headers)