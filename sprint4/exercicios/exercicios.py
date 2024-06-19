from functools import reduce
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

# Questão 1

with open(current_dir + '/data/number.txt') as arquivo:
    dados = list(map(int, arquivo.readlines()))

pares = list(filter(lambda x: x % 2 == 0, dados))

maioresPares = sorted(pares, reverse=True)[:5]

# print(maioresPares)
# print(sum(maioresPares))

# Questão 2

def conta_vogais(texto: str) -> int:
    return len(
        list(
            filter(
                lambda x: x in ['a', 'e', 'i', 'o', 'u'],
                texto.lower()
            )
        )
    )

# Questão 3


def calcula_saldo(lancamentos) -> float:
    valores = list(map(lambda x: x[0] if x[1] ==
                   'C' else -abs(x[0]), lancamentos))

    return reduce(lambda x, y: x+y, valores)

# Questão 4


def calcular_valor_maximo(operadores, operandos) -> float:
    return max(list(map(
        lambda x: eval(f'{x[1][0]} {x[0]} {x[1][1]}'),
        zip(operadores, operandos)
    )))


# Questão 5

resposta = []

with open(current_dir + '/data/estudantes.csv') as estudantes:
    for l in estudantes.readlines():

        estudante, n1, n2, n3, n4, n5 = l.strip().split(',')

        maior_nota1, maior_nota2, maior_nota3 = sorted(
            list(map(int, [n1, n2, n3, n4, n5])), reverse=True)[:3]

        media = round((maior_nota1 + maior_nota2 + maior_nota3) / 3, 2)

        resposta.append(
            f'Nome: {estudante} Notas: [{maior_nota1}, {maior_nota2}, {maior_nota3}] Média: {media}')

# for r in sorted(resposta):
#     print(r)

# Questão 6


def maiores_que_media(conteudo: dict) -> list:

    lista1 = list(map(lambda x: (x[0], float(x[1])), conteudo.items()))

    media = sum(map(lambda x: x[1], lista1)) / len(lista1)

    return sorted([y for y in lista1 if y[1] >= media], key=lambda x: x[1])

# Questão 7

# Solução 1
def pares_ate(n: int):
    for par in range(2, n+1,2):
        yield par

# Solução 2
# lista = list(filter(lambda x: x % 2 == 0, range(2, n + 1)))
# for par in lista:
#     yield par
