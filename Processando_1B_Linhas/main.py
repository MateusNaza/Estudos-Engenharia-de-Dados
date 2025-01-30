import boto3
from botocore.exceptions import ClientError

'''
Lembrando que antes de iniciar o código deve-se utilizar o comando bash awsconfigure 
e preencher com os dados de usuário aws
'''
session = boto3.Session()
s3 = session.client('s3')


# ---- Funções ----

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


# ---- Variáveis ----

bucket_name = 'processando_1B_linhas'


# ---- Criação do Bucket ----
if not bucket_exists(bucket_name):
    create_bucket(bucket_name)


# ---- Inserindo arquivos no Bucket ----



