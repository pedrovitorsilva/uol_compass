from datetime import datetime
import requests
import json
import boto3
import os

# CONSTANTES
API_KEY = os.getenv('API_KEY')
BUCKET = 'pedro-silva-desafio'
DATALAKE = "datalake-pedro-silva"
DATA_DE_PROCESSAMENTO = datetime.today().strftime('%Y/%m/%d')
DIRETORIO_GRAVACAO = f'{DATALAKE}/Raw/TMDB/JSON/{DATA_DE_PROCESSAMENTO}/movies_info.json'
FILMES_URL = 'https://api.themoviedb.org/3/discover/movie'
DETALHES_URL = 'https://api.themoviedb.org/3/movie/{movie_id}'
KEYWORDS_URL = 'https://api.themoviedb.org/3/movie/{movie_id}/keywords'


def api_call(url, parametros):
    resposta = requests.get(url, parametros)
    if resposta.status_code != 200:
        return False
    else:
        return resposta.json()


def lambda_handler(event, context):
    # Lista para armazenar informações dos filmes
    filmes_info = []

    # Realizar a consulta 10 vezes, para coletar 10 páginas de arquivos
    for i in range(1, 10):
        PARAMETROS_TMDB = {
            'api_key': API_KEY,
            'sort_by': 'popularity.desc',
            'page': i,
            'include_adult': 'false',
            'include_video': 'false',
            'primary_release_date.gte': '1980-01-01',
            'primary_release_date.lte': '1999-12-31',
            'with_genres': '878'
        }

        # Obter IDs do TMDB
        requisicao_ids_tmdb = api_call(FILMES_URL, PARAMETROS_TMDB)

        if requisicao_ids_tmdb:
            filmes = requisicao_ids_tmdb['results']
            filme_ids = [filme['id'] for filme in filmes]
        else:
            print(f"Erro na coleta dos IDs.")
            continue

        for id in filme_ids:

            if (id == 253935):
                continue

            # Obter detalhes do filme
            requisicao_detalhes = api_call(
                DETALHES_URL.format(movie_id=id),
                parametros={
                    'api_key': API_KEY
                }
            )

            if requisicao_detalhes:
                detalhes = requisicao_detalhes
            else:
                print(f"Erro na coleta de detalhes do filme {id}.")
                continue

            # Obter palavras-chave do filme
            requisicao_palavras_chave = api_call(
                KEYWORDS_URL.format(movie_id=id),
                parametros={
                    'api_key': API_KEY
                }
            )

            if requisicao_palavras_chave:
                palavras_chave = requisicao_palavras_chave
            else:
                print(f"Erro na coleta de palavras-chave do filme {id}.")
                continue

            filme_info = {
                "id": detalhes.get('id'),
                "titulo": detalhes.get('title'),
                "produtoras": [produtora['name'] for produtora in detalhes.get('production_companies', [])],
                "popularidade": detalhes.get('popularity'),
                "orcamento": detalhes.get('budget'),
                "bilheteria": detalhes.get('revenue'),
                "palavras_chave": [pc['name'] for pc in palavras_chave.get('keywords', [])]
            }

            # Adicionando o dicionário à lista de filmes
            filmes_info.append(filme_info)

        print(f"Coletados dados da página {i} com sucesso!")

    # Convertendo dados para JSON
    dados_json = json.dumps(filmes_info, ensure_ascii=False, indent=4)

    # Inicializando  S3
    s3_client = boto3.client('s3')

    # Enviando o arquivo JSON para o bucket S3
    try:
        s3_client.put_object(
            Bucket=BUCKET,
            Key=DIRETORIO_GRAVACAO,
            Body=dados_json,
            ContentType='application/json'
        )
        print(f"Dados dos filmes enviados para o S3 em '{DIRETORIO_GRAVACAO}'")
    except Exception as e:
        print(f"Erro ao enviar dados para o S3: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps('Erro ao enviar dados para o S3.')
        }

    return {
        'statusCode': 200,
        'body': json.dumps('Dados dos filmes coletados e enviados para o S3 com sucesso!')
    }
