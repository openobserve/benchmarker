import base64
import json
import random
import string
from locust import HttpUser, task, between

def generate_random_string(length=50):
    """Generate a random string of specified length"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_schema():
    """Generate a schema with 50k fields"""
    schema = {}
    for i in range(50000):
        # Generate field name that's at least 50 chars
        field_name = f"field_{generate_random_string(45)}_{i}"  # 45 + length of i + underscore = >50 chars
        field_type = random.choice(['string', 'integer', 'float', 'boolean'])
        schema[field_name] = {
            "type": field_type,
            "description": generate_random_string(60),
            "example": generate_random_string(55)
        }
    return schema

def generate_random_value(field_type):
    """Generate random value based on field type"""
    if field_type == 'string':
        return generate_random_string(60)
    elif field_type == 'integer':
        return random.randint(-1000000, 1000000)
    elif field_type == 'float':
        return random.uniform(-1000000.0, 1000000.0)
    else:  # boolean
        return random.choice([True, False])

class MonitorUser(HttpUser):
    wait_time = between(1, 3)
    user = "ashish@openobserve.ai"
    password = "sU4sOHkwpZwU5Rda"
    bas64encoded_creds = base64.b64encode(bytes(f"{user}:{password}", "utf-8")).decode("utf-8")
    headers = {
        'Authorization': 'Basic ' + bas64encoded_creds,
        'Content-Type': 'application/json'
    }
    
    # Generate schema once during class initialization
    schema = generate_schema()

    def process_ndjson_line(self, line):
        """Process a single line of NDJSON, adding nested data if it's not an index line"""
        if line.strip():
            if '"index"' in line:  # Index line
                return line
            else:  # Data line
                try:
                    data = json.loads(line)
                    # Generate nested data based on schema
                    nested_data = {}
                    for field_name, field_info in self.schema.items():
                        nested_data[field_name] = generate_random_value(field_info['type'])
                    
                    # Add nested data to original document
                    data['nested_fields'] = nested_data
                    return json.dumps(data)
                except json.JSONDecodeError:
                    return line
        return line

    @task
    def test_bulk_endpoint(self):
        """Read NDJSON file and send bulk request with enhanced data"""
        with open("bulk.ndjson", "r") as file:
            lines = file.readlines()
        
        # Process each line and join them back together
        processed_lines = [self.process_ndjson_line(line) for line in lines]
        enhanced_ndjson = '\n'.join(processed_lines)
        
        # Send the enhanced bulk request
        self.client.post("/_bulk", data=enhanced_ndjson, headers=self.headers)

if __name__ == "__main__":
    schema = generate_schema()
    print(f"Generated schema with {len(schema)} fields")

    sample_field = next(iter(schema.items()))
    print("Sample field:", sample_field)