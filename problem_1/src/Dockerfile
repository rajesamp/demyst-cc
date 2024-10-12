# Stage 1: Builder stage
FROM python:3.9-alpine AS builder

# Set work directory
WORKDIR /app

# Install build dependencies
RUN apk add --no-cache gcc musl-dev

# Copy only the requirements file first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy only the necessary Python files
COPY main.py fixed_width_generator.py fixed_width_parser.py ./

# Stage 2: Final stage
FROM python:3.9-alpine

# Set work directory
WORKDIR /app

# Copy installed dependencies from builder stage
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

# Copy Python files from builder stage
COPY --from=builder /app/*.py ./

# Copy other necessary files
COPY spec.json run.sh ./

# Make run.sh executable
RUN chmod +x run.sh

# Set environment variable
ENV PYTHONUNBUFFERED=1

# Run run.sh when the container launches
CMD ["./run.sh"]