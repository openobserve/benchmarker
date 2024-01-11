import json

def convert_to_ndjson(input_file, output_file):
    header = '{"index":{ "_index": "k8s" }}\n'
    # Open the input JSON file
    with open(input_file, 'r') as file:
        data = json.load(file)

    # Open the output file in write mode
    with open(output_file, 'w') as file:
        # Iterate over each JSON object in the array
        for item in data:
            # Convert the JSON object to a string and write it to the file
            # with a newline character
            file.write(header)
            file.write(json.dumps(item) + '\n')

# File names
input_file = 'data/k8slog.json'
output_file = 'data/k8slog.ndjson'

# Convert the file
convert_to_ndjson(input_file, output_file)
