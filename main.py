import duckdb
import time
import boto3
from io import BytesIO

session = boto3.Session()
s3 = session.client('s3')

def read_parquet_from_s3(bucket, prefix):
    response = s3.list_objects_v2(Bucket=bucket, Prefix=prefix)
    arquivos = response.get('Contents', [])
    
    dfs = []
    for arquivo in arquivos:
        s3_key = arquivo['Key']
        response = s3.get_object(Bucket=bucket, Key=s3_key)
        parquet_buffer = BytesIO(response['Body'].read())
        df = duckdb.read_parquet(parquet_buffer)
        dfs.append(df)
    
    combined_df = duckdb.concat(dfs)
    return combined_df

def create_duckdb():
    df = read_parquet_from_s3('processando-1bilhao-linhas', 'output/')
    result = duckdb.sql("""
        SELECT station,
            MIN(temperature) AS min_temperature,
            CAST(AVG(temperature) AS DECIMAL(3,1)) AS mean_temperature,
            MAX(temperature) AS max_temperature
        FROM df
        GROUP BY station
        ORDER BY station
    """)
    result.show()

if __name__ == "__main__":
    start_time = time.time()
    create_duckdb()
    took = time.time() - start_time
    print(f"DuckDB Took: {took:.2f} sec")
