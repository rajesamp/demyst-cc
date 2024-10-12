import json
import csv

def parse_fixed_width_to_csv(spec_file, input_file, output_file):
    # Load the spec
    with open(spec_file, 'r') as f:
        spec = json.load(f)

    column_names = spec['ColumnNames']
    offsets = list(map(int, spec['Offsets']))
    fixed_width_encoding = spec['FixedWidthEncoding']
    delimited_encoding = spec['DelimitedEncoding']
    include_header = spec['IncludeHeader'].lower() == 'true'

    # Calculate start positions for each field
    start_positions = [sum(offsets[:i]) for i in range(len(offsets))]

    with open(input_file, 'r', encoding=fixed_width_encoding) as infile, \
         open(output_file, 'w', newline='', encoding=delimited_encoding) as outfile:
        
        writer = csv.writer(outfile)

        # Write header if specified
        if include_header:
            writer.writerow(column_names)

        # Parse each line
        for line in infile:
            # Skip the header line in the fixed-width file if it exists
            if include_header and line.strip() == ''.join(name.ljust(offset) for name, offset in zip(column_names, offsets)):
                continue

            # Extract fields based on offsets
            fields = [line[start:start+length].strip() for start, length in zip(start_positions, offsets)]
            writer.writerow(fields)

if __name__ == "__main__":
    parse_fixed_width_to_csv('spec.json', 'output_fixed_width.txt', 'output.csv')
    print("Fixed-width file parsed to CSV successfully.")