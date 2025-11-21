#!/usr/bin/env python3
"""
Script to replicate NDJSON data with different _index names.
Reads 1.ndjson and creates a new file with 100 batches, each with a different index name (locust1-locust100).
"""

def main():
    input_file = "bulk.ndjson"
    output_file = "bulk_100_indexes.ndjson"

    # Read the original file
    print(f"Reading {input_file}...")
    with open(input_file, 'r') as f:
        original_lines = f.readlines()

    print(f"Original file has {len(original_lines)} lines")

    # Write the output file with 100 batches
    print(f"Writing to {output_file}...")
    with open(output_file, 'w') as f:
        for i in range(1, 101):  # locust1 to locust100
            index_name = f"locust{i}"
            print(f"Processing {index_name}...")

            for line in original_lines:
                # Replace locust6 with the current index name
                modified_line = line.replace('"locust6"', f'"{index_name}"')
                f.write(modified_line)

    total_lines = len(original_lines) * 100
    print(f"Done! Created {output_file} with {total_lines} lines (100 batches)")

if __name__ == "__main__":
    main()
