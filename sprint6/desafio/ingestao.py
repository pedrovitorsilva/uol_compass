from dotenv import load_dotenv, find_dotenv
import os
from datetime import datetime
import boto3

load_dotenv(find_dotenv()) # Immportando credenciais do arquivo .env

session = boto3.Session(
    aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY"),
    aws_session_token = os.getenv("AWS_SESSION_TOKEN")
)

s3 = session.client('s3', region_name='us-east-1')

# Criação do bucket, caso não exista ---------------------------

try:
    s3.head_bucket(Bucket='pedro-silva-sprint6')
    print('O bucket já existe! Pulando para envio do arquivo...')
except Exception as e:
    erro = int(e.response['Error']['Code'])
    if erro == 404:
        try:
            print('O bucket não existe. Criando bucket...')
            s3.create_bucket(Bucket='pedro-silva-sprint6')
            print('Bucket criado! Enviando arquivo...')
        except Exception as e:
            print(e)
    else:
       print(e)

# Inserção dos arquivos no bucket S3 --------------------

datalake = "datalake-pedro-silva"
data_de_processamento = datetime.today().strftime('%Y/%m/%d')

diretorio_filmes = f'{datalake}/Local/CSV/movies/{data_de_processamento}/movies.csv'
s3.upload_file("movies.csv","pedro-silva-sprint6",diretorio_filmes)
print("Arquivo CSV de filmes enviado com sucesso!")

diretorio_series = f'{datalake}/Local/CSV/series/{data_de_processamento}/series.csv'
s3.upload_file("movies.csv", "pedro-silva-sprint6", diretorio_series)
print("Arquivo CSV de séries enviado com sucesso!")
