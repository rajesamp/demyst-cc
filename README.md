### `README.md`

```markdown
# Problem 1 and Problem 2

This repository contains solutions for two problems:
1. **Problem 1: Parse Fixed Width File** - Parses a fixed-width file and generates a delimited file (e.g., CSV) based on the provided specification file.
2. **Problem 2: Data Processing and Anonymization** - Processes a CSV file containing personal data and anonymizes specific columns (e.g., first name, last name, address).

## Table of Contents
- [Project Overview](#project-overview)
- [Setup](#setup)
- [Usage](#usage)
- [Testing](#testing)
- [Docker](#docker)

## Project Overview

### Problem 1: Parse Fixed Width File
The goal of this project is to parse a fixed-width file and convert it into a CSV file. The fixed-width file contains records where each field has a specific length defined in a separate specification file.

### Problem 2: Data Processing and Anonymization
The goal of this project is to anonymize personal data in a CSV file. The columns to be anonymized are specified, and the data is hashed using SHA-256.

## Setup
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Problem 1: Parse Fixed Width File
1. **Prepare Input Files:**
   - Create a fixed-width input file (`problem1/data/input.txt`).
   - Create a specification file (`problem1/data/spec.txt`) that defines the length of each field.

2. **Run the Parser:**
   ```bash
   cd problem1
   python src/main.py
   ```
   This will parse the fixed-width file and generate a CSV file (`problem1/data/output.csv`).

### Problem 2: Data Processing and Anonymization
1. **Prepare Input Files:**
   - Create a CSV input file (`problem2/data/input.csv`) with columns: `first_name`, `last_name`, `address`, `date_of_birth`.

2. **Run the Anonymizer:**
   ```bash
   cd problem2
   python src/main.py
   ```
   This will anonymize the specified columns and generate an output CSV file (`problem2/data/output.csv`).

## Testing
To run the tests for both problems, navigate to the respective `tests` directory and use `pytest`:

### Problem 1 Tests
```bash
cd problem1/tests
pytest
```

### Problem 2 Tests
```bash
cd problem2/tests
pytest
```

## Docker
To run the projects in Docker containers:

### Problem 1: Parse Fixed Width File
1. **Build the Docker Image:**
   ```bash
   cd problem1
   docker build -t fixed-width-parser .
   ```

2. **Run the Docker Container:**
   ```bash
   docker run -v $(pwd)/data:/app/data fixed-width-parser
   ```
   This will mount the `data` directory (containing input files) to the container and run the parser.

### Problem 2: Data Processing and Anonymization
1. **Build the Docker Image:**
   ```bash
   cd problem2
   docker build -t data-anonymizer .
   ```

2. **Run the Docker Container:**
   ```bash
   docker run -v $(pwd)/data:/app/data data-anonymizer
   ```
   This will mount the `data` directory (containing input files) to the container and run the anonymizer.

## Examples

### Problem 1: Parse Fixed Width File
#### Input File (`problem1/data/input.txt`)
```
RajSam123MainSt
KumarSam456ElmSt
```

#### Specification File (`problem1/data/spec.txt`)
```
4
3
5
6
```

#### Output File (`problem1/data/output.csv`)
```
Raj,Sam,123,MainSt
Kumar,Sam,456,ElmSt
```

### Problem 2: Data Processing and Anonymization
#### Input File (`problem2/data/input.csv`)
```
first_name,last_name,address,date_of_birth
Raj,Sam,123 Main St,1980-01-01
Kumar,Sam,456 Elm St,1990-02-02
```

#### Output File (`problem2/data/output.csv`)
```
first_name,last_name,address,date_of_birth
<hashed_value>,<hashed_value>,<hashed_value>,1980-01-01
<hashed_value>,<hashed_value>,<hashed_value>,1990-02-02
```

