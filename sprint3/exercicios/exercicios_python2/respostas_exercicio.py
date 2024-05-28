import os

# Obtém o caminho do diretório onde o script está localizado
script_dir = os.path.dirname(os.path.abspath(__file__))

# Constrói o caminho completo para o arquivo CSV
csv_path = os.path.join(script_dir, 'actors.csv')

dados = []


def carregar():
    try:
        with open(csv_path) as actors:
            for line in actors.readlines()[1:]:  # Remover headers

                line = line.replace('"', "").replace(" ,", ",")

                # Erro em Robert Downey Jr.

                if 'Robert Downey' in line:
                    line = line.replace(", Jr.", " Jr.")

                fields = line.split(",")
                Actor = fields[0]
                TotalGross = float(fields[1])
                NumberOfMovies = int(fields[2])
                AveragePerMovie = float(fields[3])
                Number1Movie = fields[4]
                Gross = float(fields[5].strip())

                # Adicionar ao dicionário
                dados.append({
                    "Actor": Actor,
                    "TotalGross": TotalGross,
                    "NumberOfMovies": NumberOfMovies,
                    "AveragePerMovie": AveragePerMovie,
                    "Number1Movie": Number1Movie,
                    "Gross": Gross
                })

        print('Dados carregados!')
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")


def etapa1():

    atorComMaisFilmes = max(
        dados, key=lambda a: a['NumberOfMovies']
    )

    arquivo = os.path.join(script_dir, './etapa1.txt')

    with open(arquivo, 'w') as f:
        print(f'Ator/Atriz com mais filmes foi {atorComMaisFilmes["Actor"]}, ' +
              f'com {atorComMaisFilmes["NumberOfMovies"]} filmes.', file=f)
        
    print('Etapa 1 concluída!')


def etapa2():
    media = sum(a['Gross'] for a in dados) / len(dados)

    arquivo = os.path.join(script_dir, './etapa2.txt')

    with open(arquivo, 'w') as f:
        print(
            f'A média de receita dos principais filmes é de {media},', file=f)

    print('Etapa 2 concluída!')

def etapa3():

    atorComMaiorMedia = max(
        dados, key=lambda a: a["AveragePerMovie"]
    )

    arquivo = os.path.join(script_dir, './etapa3.txt')

    with open(arquivo, 'w') as f:
        print(f'Ator/Atriz com maior média de receita foi { atorComMaiorMedia["Actor"]}', file=f)

    print('Etapa 3 concluída!')

def etapa4():
    filmes = [a['Number1Movie'] for a in dados]

    contagem = {}

    for f in filmes:
        if f in contagem:
            contagem[f] += 1
        else:
            contagem[f] = 1

    contagem = dict(sorted(contagem.items(), key= lambda item: item[1], reverse=True))

    arquivo = os.path.join(script_dir, './etapa4.txt')

    with open(arquivo, 'w') as f:
        contador = 0
        for novoFilme, quantidade in contagem.items():
            print(f'{contador} - O filme {novoFilme} aparece {quantidade} vez(es) no dataset.', file=f)
            contador += 1
    
    print('Etapa 4 concluída!')

def etapa5():
    
    atoresReceita = [ [a['Actor'],a['TotalGross']] for a in dados]
    atoresReceita.sort(key=lambda x: x[1], reverse=True)

    arquivo = os.path.join(script_dir, './etapa5.txt')

    with open(arquivo, 'w') as f:
        for a in atoresReceita:
            print(f'{a[0]} - {a[1]}', file=f)

    print('Etapa 5 concluída!')


if __name__ == '__main__':
    carregar()

    etapa1()
    etapa2()
    etapa3()
    etapa4()
    etapa5()
