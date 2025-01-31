import boto3
import pandas as pd
from botocore.exceptions import ClientError
import pyarrow.parquet as pq

from io import BytesIO

session = boto3.Session()
s3 = session.client('s3')

def read_s3_files(bucket_name, s3_prefix):
    # Criar uma sessão com o usuário AWS
    session = boto3.Session()

    # Criar um cliente S3
    s3 = session.client('s3')

    try:
        # Listar todos os objetos no prefixo especificado
        response = s3.list_objects_v2(Bucket=bucket_name, Prefix=s3_prefix)
        arquivos = response.get('Contents', [])

        # Lista para armazenar DataFrames
        dfs = []

        # Ler e processar cada arquivo Parquet
        for arquivo in arquivos:
            s3_key = arquivo['Key']
            response = s3.get_object(Bucket=bucket_name, Key=s3_key)
            parquet_buffer = BytesIO(response['Body'].read())
            df = pq.read_table(parquet_buffer).to_pandas()
            dfs.append(df)

        # Combinar todos os DataFrames em um único DataFrame
        combined_df = pd.concat(dfs, ignore_index=True)
        print(combined_df.info())
    except Exception as e:
        print(f'Erro ao ler arquivo Parquet: {e}')
        return None

read_s3_files('processando-1bilhao-linhas', 'output/medicoes_1000000000.parquet')