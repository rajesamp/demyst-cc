import json
import random
import string
from datetime import datetime, timedelta
import sys

def load_spec(spec_file):
    try:
        with open(spec_file, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading spec file: {e}")
        sys.exit(1)

def generate_field_data(length):
    if length <= 3:
        return str(random.randint(0, 999)).zfill(length)
    elif length <= 8:
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    else:
        start_date = datetime(1950, 1, 1)
        end_date = datetime.now()
        random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
        return random_date.strftime("%Y-%m-%d %H:%M:%S")

def generate_fixed_width_file(spec_file, output_file, num_rows=100):
    spec = load_spec(spec_file)
    
    column_names = spec['ColumnNames']
    offsets = [int(offset) for offset in spec['Offsets']]
    encoding = spec['FixedWidthEncoding']
    include_header = spec['IncludeHeader'].lower() == 'true'
    
    try:
        with open(output_file, 'w', encoding=encoding) as f:
            if include_header:
                header = ''.join(f"{name:<{offset}}" for name, offset in zip(column_names, offsets))
                f.write(header + '\n')
            
            for _ in range(num_rows):
                row = ''.join(generate_field_data(offset).ljust(offset) for offset in offsets)
                f.write(row + '\n')
    except IOError as e:
        print(f"Error writing to output file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <spec_file> <output_file> [num_rows]")
        sys.exit(1)
    
    spec_file = sys.argv[1]
    output_file = sys.argv[2]
    num_rows = int(sys.argv[3]) if len(sys.argv) > 3 else 100
    
    generate_fixed_width_file(spec_file, output_file, num_rows)
    print("Fixed-width file generated successfully.")