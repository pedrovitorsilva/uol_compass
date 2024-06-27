import boto3
import os
import pandas as pd
import sqlite3
from tabulate import tabulate

PROFILE = 'profile AdministratorAccess-339712984199'

DIRETORIO_ATUAL = os.path.dirname(os.path.realpath(__file__))
ARQUIVO = 'consumo-de-agua-2022-em-m3.csv'
ENDERECO_ARQUIVO = os.path.join(DIRETORIO_ATUAL, ARQUIVO)


def iniciar_sessao_s3(profile):
    session = boto3.Session(profile_name=profile)

    return session.client('s3')


def baixar_arquivo(s3):
    s3.download_file(
        'sprint5', 'consumo-de-agua-2022-em-m3.csv', ENDERECO_ARQUIVO)


def executar_query():

    # Criando tabela ----------------------------------

    # Read the CSV file into a DataFrame
    df = pd.read_csv(ENDERECO_ARQUIVO)

    conexao = sqlite3.connect(':memory:')

    # Write the DataFrame to a SQLite table
    df.to_sql('df', conexao, index=False, if_exists='replace')

    # Lendo e Executando Query
    ENDERECO_QUERY = os.path.join(DIRETORIO_ATUAL, 'query.sql')

    with open(ENDERECO_QUERY, 'r') as file:
        query = file.read()

    resultado = pd.read_sql_query(query, conexao)

    # Fechar coneção
    conexao.close()

    return resultado


if __name__ == '__main__':

    sessao_s3 = iniciar_sessao_s3(PROFILE)

    baixar_arquivo(sessao_s3)

    resultado = executar_query()

    print(
        tabulate(
            resultado,
            headers=[
                'Local',
                'Média de Consumo (em m³)',
                'Perfil de Consumo',
                'Mês de Maior Consumo',
                'Maior Consumo (em m³)'],
            tablefmt='fancy_grid'))
