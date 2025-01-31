import boto3
from botocore.exceptions import ClientError
import pandas as pd
from io import StringIO

import create_csv
import aws_utils as util

'''
Lembrando que antes de iniciar o código deve-se utilizar o comando bash aws configure 
e preencher com os dados de usuário aws
'''
session = boto3.Session()
s3 = session.client('s3')

# Variáveis
bucket_name = 'processando-1bilhao-linhas'
num_registros = 1_000_000_000
file_name = 'data/amostra_44k.csv'
s3_key = 'sample/amostra_44k.csv'

# Criando Bucket se não existir
if not util.bucket_exists(bucket_name):
    util.create_bucket(bucket_name)

# # Subindo arquivo de amostra para o bucket
# util.upload_file_to_s3(file_name, bucket_name, s3_key)

util.process_csv_from_s3(bucket_name, s3_key)

# # ---- Inserindo arquivos no Bucket ----
# create_csv.gerar_dados_teste(num_registros)


