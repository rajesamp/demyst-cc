# Stage 1: Build stage
FROM python:3.8-slim as builder

# Set the working directory
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Stage 2: Final stage
FROM python:3.8-slim

# Set the working directory
WORKDIR /usr/src/app

# Copy the installed dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy the application code
COPY . .

# Run the script to generate the CSV file
CMD ["python", "generate_csv.py"]