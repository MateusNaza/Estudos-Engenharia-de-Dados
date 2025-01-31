import boto3
from botocore.exceptions import ClientError
import pandas as pd
from io import StringIO
import pyarrow as pa
import pyarrow.parquet as pq
from io import BytesIO

session = boto3.Session()
s3 = session.client('s3')

def bucket_exists(bucket_name):
    try:       
        s3.head_bucket(Bucket=bucket_name)
        return True
    except ClientError:
        return False


def create_bucket(bucket_name, region=None):
    try:
        if region is None:
            s3.create_bucket(Bucket=bucket_name)
        else:
            location = {'LocationConstraint': region}
            s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)

        print(f"Bucket '{bucket_name}' criado com sucesso.")
    except ClientError:
        print(f'Falha na criação do bucket!')


def process_csv_from_s3(bucket_name, s3_key):
    try:
        response = s3.get_object(Bucket=bucket_name, Key=s3_key)
        
        content = response['Body'].read().decode('utf-8')
        
        df = pd.read_csv(StringIO(content), skiprows=2, sep=';', header=None, names=['City', 'Temperature'])

        return df
        
    except Exception as e:
        print(f"Erro ao processar o arquivo CSV: {e}")


def upload_file_to_s3(file_name, bucket_name, s3_key):
    try:
        s3.upload_file(file_name, bucket_name, s3_key)
        print(f"Arquivo '{file_name}' enviado com sucesso para o bucket '{bucket_name}' com a chave '{s3_key}'.")
    except ClientError as e:
        print(f"Erro ao enviar o arquivo: {e}")


def delete_file_from_s3(bucket_name, s3_key):
    try:
        s3.delete_object(Bucket=bucket_name, Key=s3_key)
        print(f"Arquivo '{s3_key}' deletado com sucesso do bucket '{bucket_name}'.")
    except ClientError as e:
        print(f"Erro ao deletar o arquivo: {e}")


def save_parquet(lote_dados, bucket_name, s3_key):
    """
    Salva um lote de dados no formato Parquet diretamente no S3.
    """
    df = pd.DataFrame(lote_dados, columns=["station", "temperature"])
    table = pa.Table.from_pandas(df)

    # Converter o DataFrame para Parquet
    parquet_buffer = BytesIO()
    pq.write_table(table, parquet_buffer)

    try:
        # Enviar o Parquet para o S3
        s3.put_object(Bucket=bucket_name, Key=s3_key, Body=parquet_buffer.getvalue())
        print(f"Dados enviados com sucesso para o bucket '{bucket_name}' com a chave '{s3_key}'.")
    except Exception as e:
        print(f"Erro ao enviar os dados para o S3: {e}")