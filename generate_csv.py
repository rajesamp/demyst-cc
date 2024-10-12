import csv
import random
import string
from datetime import datetime, timedelta

def generate_random_name(length=5):
    return ''.join(random.choices(string.ascii_letters, k=length))

def generate_random_address():
    return f"{random.randint(1, 100)} {generate_random_name(6)} St."

def generate_random_date_of_birth():
    start_date = datetime(1950, 1, 1)
    end_date = datetime(2000, 12, 31)
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_date.strftime("%Y-%m-%d")

def generate_csv_file(output_file, num_rows=1000000):
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['first_name', 'last_name', 'address', 'date_of_birth'])
        for _ in range(num_rows):
            first_name = generate_random_name()
            last_name = generate_random_name()
            address = generate_random_address()
            date_of_birth = generate_random_date_of_birth()
            writer.writerow([first_name, last_name, address, date_of_birth])

if __name__ == "__main__":
    generate_csv_file('output_data.csv', num_rows=1000000)
    print("CSV file generated successfully.")