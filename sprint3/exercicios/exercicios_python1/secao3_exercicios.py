## Copia dos exercícios do arquivo .ipynb
## Exercícios 1 ao 5

####### Exercício 1

# Desenvolva um código em Python que crie variáveis para armazenar o nome e a idade de uma pessoa, 
# juntamente com seus valores correspondentes. 
# Como saída, imprima o ano em que a pessoa completará 100 anos de idade.

from datetime import date

nome = "Pedro"
idade = 21

print(date.today().year + (100 - idade))

####### Exercício 2

# Escreva um código Python que use a função range() para adicionar três números em uma lista
# e verificar se esses três números são pares ou ímpares. 

# Para cada número, imprima como saída Par: ou Ímpar: e o número correspondente 
# (um linha para cada número lido).

# Importante: Aplique a função range() em seu código.
# Exemplos de saída:
# - Par: 2
# - Ímpar: 3

numeros = [x for x in range(1, 4)]  # 1,2,3

for n in numeros:
    if n % 2 == 0:
        print(f"Par: {n}")
    else:
        print(f"Ímpar: {n}")

####### Exercício 3

# Escreva um código Python para imprimir os números pares de 0 até 20 (incluso).
# Importante: Aplique a função range() em seu código.

for i in range(0, 21, 2):
    print(i)

####### Exercício 4

# Escreva um código Python para imprimir todos os números primos entre 1 até 100. 
# Lembre-se que você deverá desenvolver o cálculo que identifica se um número é primo ou não.
# Importante: Aplique a função range().

# Referências:
# Sieve of Eratosthenes - https://pt.wikipedia.org/wiki/Crivo_de_Erat%C3%B3stenes

LIMITE = 100

# Todos os números
numeros = [n for n in range(2, LIMITE + 1)]

# Todos os números, inicialmente, seriam primos
primos = numeros

# Menor Valor
num_atual = numeros[0]

# Enquanto o número atual for menor que a raiz de limite
while num_atual * num_atual <= LIMITE:

    # Se o número for primo, remova todos os seus múltiplos da lista (se estiverem lá)
    if num_atual in primos:

        for i in range(num_atual * num_atual, LIMITE + 1, num_atual):
            if i in numeros:
                numeros.remove(i)

    primos = numeros
    num_atual += 1

print(primos)
# for n in primos:
#     print(n)

####### Exercício 5

# Escreva um código Python que declara 3 variáveis:
# - dia, inicializada com valor 22
# - mes, inicializada com valor 10 e
# - ano, inicializada com valor 2022
# Como saída, você deverá imprimir a data correspondente, no formato a seguir dia/mes/ano.

dia, mes, ano = 22, 10, 2022

print(f"{dia}/{mes}/{ano}")
