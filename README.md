# demyst-cc
# Problem - 1
# Fixed-Width File Processor

This project provides a Docker-based solution for generating fixed-width files and parsing them into CSV format. It's designed to be flexible, allowing customization through a JSON specification file.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Project Structure](#project-structure)
- [Setup](#setup)
- [Usage](#usage)
- [Docker Commands](#docker-commands)
- [Customization](#customization)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)

## Features

- Generate fixed-width files based on a JSON specification
- Parse fixed-width files into CSV format
- Flexible column configuration
- Customizable encodings for input and output files
- Docker-based for easy deployment and use
- Command-line interface for easy integration

## Requirements

- Docker
- Git (for version control and cloning the repository)

## Project Structure

```
fixed-width-processor/
│
├── Dockerfile
├── .dockerignore
├── requirements.txt
├── run.sh
├── main.py
├── fixed_width_generator.py
├── fixed_width_parser.py
├── spec.json
└── README.md
```

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/your-username/fixed-width-processor.git
   cd fixed-width-processor
   ```

2. Build the Docker image:
   ```
   docker build -t fixed-width-processor .
   ```

## Usage

Run the Docker container with default settings:

```
docker run -v $(pwd):/app/output fixed-width-processor
```

This will generate a fixed-width file (`output_fixed_width.txt`) and a CSV file (`output.csv`) in your current directory.

### Custom Arguments

You can customize the process with the following arguments:

- `--spec`: Path to the spec file (default: "spec.json")
- `--fixed-width`: Path for the fixed-width output file (default: "output_fixed_width.txt")
- `--csv`: Path for the CSV output file (default: "output.csv")
- `--rows`: Number of rows to generate (default: 100)

Example with custom arguments:

```
docker run -v $(pwd):/app/output fixed-width-processor --spec custom_spec.json --rows 200 --fixed-width custom_fixed.txt --csv custom_output.csv
```

## Docker Commands

- Build the image: `docker build -t fixed-width-processor .`
- Run the container: `docker run -v $(pwd):/app/output fixed-width-processor`
- Remove the image: `docker rmi fixed-width-processor`

## Customization

You can customize the fixed-width file generation by modifying the `spec.json` file. The specification includes:

- `ColumnNames`: List of column names
- `Offsets`: List of column widths
- `FixedWidthEncoding`: Encoding for the fixed-width file
- `DelimitedEncoding`: Encoding for the CSV file
- `IncludeHeader`: Whether to include a header row (true/false)

Example `spec.json`:

```json
{
    "ColumnNames": ["id", "name", "date"],
    "Offsets": ["5", "15", "10"],
    "FixedWidthEncoding": "utf-8",
    "DelimitedEncoding": "utf-8",
    "IncludeHeader": "true"
}
```

## Error Handling

The application includes error handling for common issues:

- File not found
- JSON parsing errors
- I/O errors when reading or writing files

If an error occurs, the application will print an error message and exit with a non-zero status code.

## Optimized Docker image

I have used multi-build approach to cut short image size and it's currently at 60Megs
![image](https://github.com/user-attachments/assets/897d7988-02ea-444e-921f-0f30d4332c57)

# Problem 2: Data Processing

This directory contains the solution for Problem 2 of the data engineering challenge, which involves generating a CSV file with random data and anonymizing specific columns.

## Overview

### Tasks
1. **Generate a CSV File:**
   - Create a CSV file containing `first_name`, `last_name`, `address`, and `date_of_birth` fields with random data.

2. **Anonymize the Data:**
   - Process the CSV file to anonymize the data in the `first_name`, `last_name`, and `address` columns.

3. **Scalability:**
   - Ensure the solution can handle a 2GB CSV file efficiently.
   - Demonstrate scalability for larger datasets using Apache Arrow and Polars.

## Directory Structure

```plaintext
/problem2
    Dockerfile
    generate_csv.py
    anonymize_data.py
    README.md

## Tools used:
1. **Apache Arrow and Polars**
   - Apache Arrow to read the CSV file into an Arrow Table, and then convert it to a Polars DataFrame for further processing
   Use Apache Arrow to load the CSV file into an Arrow Table.
   Convert the Arrow Table to a Polars DataFrame.
   Anonymize the specified columns.
   Save the anonymized data back to a CSV file.


