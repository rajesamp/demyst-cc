import pyarrow.csv as pv
import polars as pl
import hashlib

def anonymize_data_arrow_polars(input_file, output_file):
    # Read CSV file into an Arrow Table
    table = pv.read_csv(input_file)
    
    # Convert Arrow Table to Polars DataFrame
    df = pl.DataFrame(table.to_pandas())
    
    # Anonymize the specified columns
    df = df.with_column(pl.col("first_name").apply(lambda x: hashlib.sha256(x.encode()).hexdigest()))
    df = df.with_column(pl.col("last_name").apply(lambda x: hashlib.sha256(x.encode()).hexdigest()))
    df = df.with_column(pl.col("address").apply(lambda x: hashlib.sha256(x.encode()).hexdigest()))
    
    # Save the anonymized data back to a CSV file
    df.write_csv(output_file)

if __name__ == "__main__":
    anonymize_data_arrow_polars('output_data.csv', 'anonymized_data.csv')
    print("Data anonymized successfully.")