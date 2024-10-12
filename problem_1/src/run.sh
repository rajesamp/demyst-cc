#!/bin/sh
set -e

echo "Starting Fixed-Width File Processor"

# Run the main Python script with any provided arguments
python main.py "$@"

echo "Processing complete. Check the output files in the mounted volume."