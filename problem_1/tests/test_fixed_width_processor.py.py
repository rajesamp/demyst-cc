import unittest
import json
import os
import csv
from fixed_width_generator import generate_fixed_width_file
from fixed_width_parser import parse_fixed_width_to_csv

class TestFixedWidthProcessor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spec_file = 'test_spec.json'
        cls.fixed_width_file = 'test_fixed_width.txt'
        cls.csv_file = 'test_output.csv'
        
        # Create a test spec file
        spec = {
            "ColumnNames": ["id", "name", "date"],
            "Offsets": ["5", "15", "10"],
            "FixedWidthEncoding": "utf-8",
            "DelimitedEncoding": "utf-8",
            "IncludeHeader": "true"
        }
        with open(cls.spec_file, 'w') as f:
            json.dump(spec, f)

    @classmethod
    def tearDownClass(cls):
        # Clean up test files
        for file in [cls.spec_file, cls.fixed_width_file, cls.csv_file]:
            if os.path.exists(file):
                os.remove(file)

    def test_generate_fixed_width_file(self):
        generate_fixed_width_file(self.spec_file, self.fixed_width_file, num_rows=10)
        self.assertTrue(os.path.exists(self.fixed_width_file))
        
        with open(self.fixed_width_file, 'r') as f:
            lines = f.readlines()
            self.assertEqual(len(lines), 11)  # 10 data rows + 1 header
            self.assertEqual(len(lines[0].strip()), 30)  # 5 + 15 + 10

    def test_parse_fixed_width_to_csv(self):
        generate_fixed_width_file(self.spec_file, self.fixed_width_file, num_rows=10)
        parse_fixed_width_to_csv(self.spec_file, self.fixed_width_file, self.csv_file)
        self.assertTrue(os.path.exists(self.csv_file))
        
        with open(self.csv_file, 'r') as f:
            reader = csv.reader(f)
            rows = list(reader)
            self.assertEqual(len(rows), 11)  # 10 data rows + 1 header
            self.assertEqual(rows[0], ['id', 'name', 'date'])

    def test_end_to_end(self):
        generate_fixed_width_file(self.spec_file, self.fixed_width_file, num_rows=100)
        parse_fixed_width_to_csv(self.spec_file, self.fixed_width_file, self.csv_file)
        
        with open(self.csv_file, 'r') as f:
            reader = csv.reader(f)
            rows = list(reader)
            self.assertEqual(len(rows), 101)  # 100 data rows + 1 header
            self.assertEqual(len(rows[1]), 3)  # 3 columns

if __name__ == '__main__':
    unittest.main()