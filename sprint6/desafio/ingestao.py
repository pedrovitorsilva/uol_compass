from dotenv import load_dotenv, find_dotenv
import os
from datetime import datetime
import boto3

load_dotenv(find_dotenv())  # Immportando credenciais do arquivo .env

BUCKET = 'pedro-silva-desafio'
DATALAKE = "datalake-pedro-silva"
DATA_DE_PROCESSAMENTO = datetime.today().strftime('%Y/%m/%d')

diretorio_filmes = f'{DATALAKE}/Raw/Local/CSV/movies/{DATA_DE_PROCESSAMENTO}/movies.csv'
diretorio_series = f'{DATALAKE}/Raw/Local/CSV/series/{DATA_DE_PROCESSAMENTO}/series.csv'

session = boto3.Session(
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    aws_session_token=os.getenv("AWS_SESSION_TOKEN")
)

s3 = session.client('s3', region_name='us-east-1')

# Criação do bucket, caso não exista (caso haja erro 404) ---------------------------

def criar_bucket():

    try:
        s3.head_bucket(Bucket=BUCKET)
        print('O bucket já existe! Pulando para envio do arquivo...')

    except Exception as e:
        erro = int(e.response['Error']['Code'])
        if erro == 404:
            try:
                print('O bucket não existe. Criando bucket...')
                s3.create_bucket(Bucket=BUCKET)
                print('Bucket criado! Pulando para envio do arquivo...')
            except Exception as e:
                print(e)
        else:
            print(e)

# Inserção dos arquivos no bucket S3 --------------------

def enviar_arquivo(diretorio, arquivo, nome):

    print(f'Enviando CSV de {nome}...')

    try:
        s3.head_object(Bucket=BUCKET, Key=diretorio)
        print(f'Arquivo CSV de {nome} já existe no S3!')

    except Exception as e:
        erro = int(e.response['Error']['Code'])
        if erro == 404:
            try:
                s3.upload_file(arquivo, BUCKET, diretorio)
                print(f"Arquivo CSV de {nome} enviado com sucesso no S3!")
            except Exception as e:
                print(e)
        else:
            print(e)

if __name__ == '__main__':
    criar_bucket()
    enviar_arquivo(diretorio_filmes, "movies.csv", 'filmes')
    enviar_arquivo(diretorio_series, "series.csv", 'séries')
