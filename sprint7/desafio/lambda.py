from dotenv import load_dotenv, find_dotenv
import os
import requests
import json

load_dotenv(find_dotenv())  # Importando credenciais do arquivo .env

# CONSTANTES
API_KEY = os.getenv("API_KEY")

FILMES_URL = 'https://api.themoviedb.org/3/discover/movie'
DETALHES_URL = 'https://api.themoviedb.org/3/movie/{movie_id}'
KEYWORDS_URL = 'https://api.themoviedb.org/3/movie/{movie_id}/keywords'


def api_call(url, parametros):
    resposta = requests.get(url, parametros)
    if resposta.status_code != 200:
        return False
    else:
        return resposta.json()


# Lista para armazenar informações dos filmes
filmes_info = []

# Realizar a consulta 2 vezes, para coletar 2 páginas de arquivos
for i in range(1, 3):
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

    for id in filme_ids:
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

# Salvando em um arquivo JSON
with open('filmes_info.json', 'w', encoding='utf-8') as f:
    json.dump(filmes_info, f, ensure_ascii=False, indent=4)

print("Dados dos filmes salvos em 'filmes_info.json'")
