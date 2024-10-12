import csv
import hashlib
import pytest

@pytest.fixture
def setup_csv_files(tmpdir):
    input_file = tmpdir.join("input.csv")
    output_file = tmpdir.join("output.csv")
    
    input_content = "first_name,last_name,address,date_of_birth\nJohn,Doe,123 Main St,1980-01-01\nJane,Doe,456 Elm St,1990-02-02"
    
    input_file.write(input_content)
    
    return str(input_file), str(output_file)

def test_anonymize_data(setup_csv_files):
    input_file, output_file = setup_csv_files
    
    anonymize_data(input_file, output_file, ['first_name', 'last_name', 'address'])
    
    with open(output_file, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
    
    expected_hashes = {
        'first_name': hashlib.sha256('John'.encode('utf-8')).hexdigest(),
        'last_name': hashlib.sha256('Doe'.encode('utf-8')).hexdigest(),
        'address': hashlib.sha256('123 Main St'.encode('utf-8')).hexdigest(),
    }
    
    assert rows[0]['first_name'] == expected_hashes['first_name']
    assert rows[0]['last_name'] == expected_hashes['last_name']
    assert rows[0]['address'] == expected_hashes['address']
    assert rows[0]['date_of_birth'] == '1980-01-01'

def test_empty_file(setup_csv_files):
    input_file, output_file = setup_csv_files
    
    with open(input_file, 'w', encoding='utf-8') as infile:
        infile.write("")
    
    anonymize_data(input_file, output_file, ['first_name', 'last_name', 'address'])
    
    with open(output_file, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
    
    assert rows == []

def test_single_record(setup_csv_files):
    input_file, output_file = setup_csv_files
    
    with open(input_file, 'w', encoding='utf-8') as infile:
        infile.write("first_name,last_name,address,date_of_birth\nJohn,Doe,123 Main St,1980-01-01")
    
    anonymize_data(input_file, output_file, ['first_name', 'last_name', 'address'])
    
    with open(output_file, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
    
    expected_hashes = {
        'first_name': hashlib.sha256('John'.encode('utf-8')).hexdigest(),
        'last_name': hashlib.sha256('Doe'.encode('utf-8')).hexdigest(),
        'address': hashlib.sha256('123 Main St'.encode('utf-8')).hexdigest(),
    }
    
    assert rows[0]['first_name'] == expected_hashes['first_name']
    assert rows[0]['last_name'] == expected_hashes['last_name']
    assert rows[0]['address'] == expected_hashes['address']
    assert rows[0]['date_of_birth'] == '1980-01-01'

def test_multiple_records(setup_csv_files):
    input_file, output_file = setup_csv_files
    
    with open(input_file, 'w', encoding='utf-8') as infile:
        infile.write("first_name,last_name,address,date_of_birth\nJohn,Doe,123 Main St,1980-01-01\nJane,Doe,456 Elm St,1990-02-02")
    
    anonymize_data(input_file, output_file, ['first_name', 'last_name', 'address'])
    
    with open(output_file, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
    
    expected_hashes = {
        'first_name': hashlib.sha256('John'.encode('utf-8')).hexdigest(),
        'last_name': hashlib.sha256('Doe'.encode('utf-8')).hexdigest(),
        'address': hashlib.sha256('123 Main St'.encode('utf-8')).hexdigest(),
    }
    
    assert rows[0]['first_name'] == expected_hashes['first_name']
    assert rows[0]['last_name'] == expected_hashes['last_name']
    assert rows[0]['address'] == expected_hashes['address']
    assert rows[0]['date_of_birth'] == '1980-01-01'
    
    expected_hashes = {
        'first_name': hashlib.sha256('Jane'.encode('utf-8')).hexdigest(),
        'last_name': hashlib.sha256('Doe'.encode('utf-8')).hexdigest(),
        'address': hashlib.sha256('456 Elm St'.encode('utf-8')).hexdigest(),
    }
    
    assert rows[1]['first_name'] == expected_hashes['first_name']
    assert rows[1]['last_name'] == expected_hashes['last_name']
    assert rows[1]['address'] == expected_hashes['address']
    assert rows[1]['date_of_birth'] == '1990-02-02'