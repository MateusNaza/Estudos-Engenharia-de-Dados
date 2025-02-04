import duckdb
import boto3 
import time

import aws_utils as util

conn = duckdb.connect() # Iniciando conexão com o duckdb

# Conexão com aws no duckdb
conn.execute("INSTALL aws")
conn.execute("LOAD aws")
conn.execute("CALL load_aws_credentials()") 

query = """
SELECT station,
            MIN(temperature) AS min_temperature,
            CAST(AVG(temperature) AS DECIMAL(3,1)) AS mean_temperature,
            MAX(temperature) AS max_temperature
        FROM read_parquet(?)
        GROUP BY station
        ORDER BY station
"""

s3_path = f's3://processando-1bilhao-linhas/output/*.parquet'

start_time = time.time() # Começa a contar a execução

result = conn.execute(query, [s3_path]).fetchdf()

took = time.time() - start_time # Encerra a contagem de tempo de execução

conn.close() # Encerrando conexão com o duckdb

print(result)
print(f"DuckDB Took: {took:.2f} sec")