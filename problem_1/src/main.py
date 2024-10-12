import argparse
import sys
from fixed_width_generator import generate_fixed_width_file
from fixed_width_parser import parse_fixed_width_to_csv

def process_fixed_width_data(spec_file, fixed_width_output, csv_output, num_rows=100):
    print(f"Generating fixed-width file with {num_rows} rows...")
    generate_fixed_width_file(spec_file, fixed_width_output, num_rows)
    print(f"Fixed-width file generated: {fixed_width_output}")

    print(f"Parsing fixed-width file to CSV...")
    parse_fixed_width_to_csv(spec_file, fixed_width_output, csv_output)
    print(f"CSV file generated: {csv_output}")

    # Print a sample of the generated data
    print("\nSample of generated data:")
    try:
        with open(csv_output, 'r') as f:
            for _ in range(5):  # Print first 5 lines
                print(f.readline().strip())
    except IOError as e:
        print(f"Error reading CSV file: {e}")
    print("...")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process fixed-width file to CSV")
    parser.add_argument("--spec", default="spec.json", help="Path to the spec file")
    parser.add_argument("--fixed-width", default="output_fixed_width.txt", help="Path for the fixed-width output file")
    parser.add_argument("--csv", default="output.csv", help="Path for the CSV output file")
    parser.add_argument("--rows", type=int, default=100, help="Number of rows to generate")

    args = parser.parse_args()

    try:
        process_fixed_width_data(args.spec, args.fixed_width, args.csv, args.rows)
        print("\nProcess completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)