import os
# Copia dos exercícios do arquivo .ipynb
# Exercícios 6 a 25

# Exercício 6

# Considere as duas listas abaixo:
#
#
# `a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]`
#
# `b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]`
#
#
# Escreva um programa para avaliar o que ambas as listas têm em comum (sem repetições),
# imprimindo a lista de valores da interseção na saída padrão.

import random
import json
a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

intersecao = set(a).intersection(set(b))
print(list(intersecao))

# Exercício 7
# Dada a seguinte lista:
#
# `a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]`
#
# Faça um programa que gere uma nova lista contendo apenas números ímpares.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

b = list(filter(lambda x: x % 2 != 0, a))
print(b)


# Exercício 8
# Verifique se cada uma das palavras da lista ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']
# é ou não um palíndromo.

# Palíndromo é uma palavra que permanece igual se lida de traz pra frente.

# É necessário que você imprima no console exatamente assim:

# - A palavra: maça não é um palíndromo
# - A palavra: arara é um palíndromo
# - A palavra: audio não é um palíndromo
# - A palavra: radio não é um palíndromo
# - A palavra: radar é um palíndromo
# - A palavra: moto não é um palíndromo

lista = ["maça", "arara", "audio", "radio", "radar", "moto"]


def palindromo(palavra):
    ponteiro1 = 0
    ponteiro2 = len(palavra) - 1

    while ponteiro1 <= ponteiro2:

        if palavra[ponteiro1] != palavra[ponteiro2]:
            return False

        ponteiro1 += 1
        ponteiro2 -= 1

    return True


for palavra in lista:
    print(
        f'A palavra: {palavra} {"" if palindromo(palavra) else "não " }é um palíndromo'
    )

# Exercício 9
# Dada as listas a seguir:
#
#
# - primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
# - sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
# - idades = [19, 28, 25, 31]
#
# Faça um programa que imprima o dados na seguinte estrutura:
# "índice - primeiroNome sobreNome está com idade anos".
#
# Exemplo: 0 - João Soares está com 19 anos

primeirosNomes = ["Joao", "Douglas", "Lucas", "José"]
sobreNomes = ["Soares", "Souza", "Silveira", "Pedreira"]
idades = [19, 28, 25, 31]

for dado in enumerate(tuple(zip(primeirosNomes, sobreNomes, idades))):
    indice = dado[0]
    pn, sn, i = dado[1]
    print(f"{indice} - {pn} {sn} está com {i} anos")

# Exercício 10
# Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados.
# Utilize a lista a seguir para testar sua função.
#
#
# ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

lista = ["abc", "abc", "abc", "123", "abc", "123", "123"]


def remover_duplicados(l):
    return list(set(l))


print(remover_duplicados(lista))


# Exercício 11

# Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.

script_dir = os.path.dirname(os.path.abspath(__file__))
arquivo_json = os.path.join(script_dir, "./data/person.json")

with open(arquivo_json) as file:
    f = file.read()
    dados = json.loads(f)
    print(dados)

# Exercício 12

# Implemente a função my_map(list, f) que recebe uma lista como primeiro argumento e
# uma função como segundo argumento. Esta função aplica a função recebida para cada elemento da lista recebida e retorna o resultado em uma nova lista.
#
#
# Teste sua função com a lista de entrada [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] e com uma função que potência de 2 para cada elemento.


def my_map(l, f): return list(map(f, l))


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_map(lista, lambda x: x**2))

# Exercício 13

# Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt e imprime o seu conteúdo.

script_dir = os.path.dirname(os.path.abspath(__file__))
arquivo_txt = os.path.join(script_dir, './data/arquivo_texto.txt')

with open(arquivo_txt) as file:
    dados = file.read().strip()

print(dados)

# Exercício 14

# Escreva uma função que recebe um número variável de parâmetros não nomeados e um número variado de parâmetros nomeados e imprime o valor de cada parâmetro recebido.
#
#
# Teste sua função com os seguintes parâmetros:
#
#
# (1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)


def funcao(*args, **kwargs):
    for i in args:
        print(i)
    for j in kwargs.values():
        print(j)


funcao(1, 3, 4, "hello", parametro_nomeado="alguma coisa", x=20)

# Exercício 15

# Implemente a classe Lampada. A classe Lâmpada recebe um booleano no seu construtor, Truese a lâmpada estiver ligada, False caso esteja desligada. A classe Lampada possuí os seguintes métodos:
#
# - liga(): muda o estado da lâmpada para ligada
#
# - desliga(): muda o estado da lâmpada para desligada
#
# - esta_ligada(): retorna verdadeiro se a lâmpada estiver ligada, falso caso contrário
#
# Para testar sua classe:
#
# - Ligue a Lampada
#
# - Imprima: A lâmpada está ligada? True
#
# - Desligue a Lampada
#
# - Imprima: A lâmpada ainda está ligada? False


class Lampada:
    def __init__(self, ligada):
        self.ligada = ligada

    def liga(self):
        self.ligada = True

    def desliga(self):
        self.ligada = False

    def esta_ligada(self):
        return self.ligada


lamp = Lampada(True)
print(lamp.esta_ligada())
lamp.desliga()
print(lamp.esta_ligada())

# Exercício 16

# Escreva uma função que recebe uma string de números separados por vírgula e retorne a soma de todos eles. Depois imprima a soma dos valores.

string = "1,3,4,6,10,76"


def func(s):
    return sum(map(lambda x: int(x), s.split(",")))


print(func(string))

# Exercício 17

# Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas: a lista recebida dividida em 3 partes iguais.

# def dividir(lista):
#     partes = [[], [], []]

#     parte_atual = 0
#     for i in lista:
#         partes[parte_atual].append(i)

#         parte_atual += 1
#         if parte_atual > 2:
#             parte_atual = 0

#     return partes

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


def dividir(lista):

    tamanho_das_partes = len(lista) // 3
    parte1 = lista[:tamanho_das_partes]
    parte2 = lista[tamanho_das_partes: tamanho_das_partes * 2]
    parte3 = lista[tamanho_das_partes * 2:]

    print(parte1, parte2, parte3)
    return


dividir(lista)

# Exercício 18

# Dado o dicionário a seguir:
#
# speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
#
# Crie uma lista com todos os valores (não as chaves!) e coloque numa lista de forma que não haja valores duplicados.

speed = {
    "jan": 47,
    "feb": 52,
    "march": 47,
    "April": 44,
    "May": 52,
    "June": 53,
    "july": 54,
    "Aug": 44,
    "Sept": 54,
}

print(list(set(speed.values())))

# Exercício 19

# Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista.
#
# Obs.: Lembrem-se, para calcular a mediana a lista deve estar ordenada!


random_list = random.sample(range(500), 50)

random_list = sorted(random_list)

valor_minimo = min(random_list)
valor_maximo = max(random_list)

media = sum(random_list) / len(random_list)

# 50 números: valor par
# Mediana = somar os termos centrais e dividir por 2

len_list = len(random_list)

mediana = (random_list[len_list // 2] + random_list[(len_list // 2) - 1]) / 2

print(
    f"Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}"
)

# Exercício 20

# Imprima a lista de trás pra frente.

a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(a[::-1])

# Exercício 21

# Implemente duas classes, Pato e Pardal , que herdam de uma superclasse chamada Passaro as habilidades de voar e emitir som.
#
#
# Contudo, tanto Pato quanto Pardal devem emitir sons diferentes (de maneira escrita) no console, conforme o modelo a seguir.
#
#
# Imprima no console exatamente assim:
#
#     Pato
#     Voando...
#     Pato emitindo som...
#     Quack Quack
#     Pardal
#     Voando...
#     Pardal emitindo som...
#     Piu Piu


class Passaro:

    def __init__(self, nome, som):
        self.nome = nome
        self.som = som

    def imprimir_nome(self):
        print(self.nome)

    def voar(self):
        print("Voando...")

    def emitirSom(self):
        print(f"{self.nome} emitindo som...\n{self.som}")


class Pato(Passaro):

    def __init__(self):
        super().__init__("Pato", "Quack Quack")


class Pardal(Passaro):

    def __init__(self):
        super().__init__("Pardal", "Piu Piu")


pato = Pato()
pardal = Pardal()

pato.imprimir_nome()
pato.voar()
pato.emitirSom()

pardal.imprimir_nome()
pardal.voar()
pardal.emitirSom()

# Exercício 22

# Crie uma classe chamada Pessoa, com um atributo privado chamado nome (declarado internamente na classe como __nome) e um atributo público de nome id.
#
# Adicione dois métodos à classe, sendo um para definir o valor de __nome e outro para retornar o valor do respectivo atributo.
#
# Lembre-se que o acesso ao atributo privado deve ocorrer somente através dos métodos definidos, nunca diretamente.  Você pode alcançar este comportamento através do recurso de properties do Python.


class Pessoa:
    def __init__(self, id):
        self.id = id
        self.__nome = "Fulano De Tal"

    def _get_nome(self):
        return self.__nome

    def _set_nome(self, nome):
        self.__nome = nome

    nome = property(fget=_get_nome, fset=_set_nome)


# Exercício 23

# Crie uma classe  Calculo  que contenha um método que aceita dois parâmetros, X e Y, e retorne a soma dos dois. Nessa mesma classe, implemente um método de subtração, que aceita dois parâmetros, X e Y, e retorne a subtração dos dois (resultados negativos são permitidos).


class Calculo:
    def __init__(self):
        pass

    def soma(self, x, y):
        print(f"Somando {x}+{y} = {x + y}")

    def subtracao(self, x, y):
        print(f"Subtraindo {x}-{y} = {x + y}")


c = Calculo()
c.soma(4, 5)
c.subtracao(4, 5)

# Exercício 24

# Crie uma classe Ordenadora que contenha um atributo listaBaguncada e que contenha os métodos ordenacaoCrescente e ordenacaoDecrescente.
#
# Instancie um objeto chamado crescente dessa classe Ordenadora que tenha como listaBaguncada a lista [3,4,2,1,5] e instancie um outro objeto, decrescente dessa mesma classe com uma outra listaBaguncada sendo [9,7,6,8].
#
# Para o primeiro objeto citado, use o método ordenacaoCrescente e para o segundo objeto, use o método ordenacaoDecrescente.


class Ordenadora:
    def __init__(self, listaBaguncada):
        self.listaBaguncada = listaBaguncada

    def ordenacaoCrescente(self):
        return sorted(self.listaBaguncada)

    def ordenacaoDecrescente(self):
        return self.ordenacaoCrescente()[::-1]


a = Ordenadora([3, 4, 2, 1, 5])
b = Ordenadora([9, 7, 6, 8])

print(a.ordenacaoCrescente())
print(b.ordenacaoDecrescente())

# Exercício 25

# Crie uma classe Avião que possua os atributos modelo, velocidade_maxima, cor e capacidade.
#
# Defina o atributo cor de sua classe , de maneira que todas as instâncias de sua classe avião sejam da cor “azul”.
#
# Após isso, a partir de entradas abaixo, instancie e armazene em uma lista 3 objetos da classe Avião.
#
# Ao final, itere pela lista imprimindo cada um dos objetos no seguinte formato:
#
# “O avião de modelo “x” possui uma velocidade máxima de “y”, capacidade para “z” passageiros e é da cor “w”.
#
# Sendo x, y, z e w cada um dos atributos da classe “Avião”.
#
#
# Valores de entrada:
#
# - modelo BOIENG456: velocidade máxima 1500 km/h: capacidade para 400 passageiros: Cor Azul
#
# - modelo Embraer Praetor 600: velocidade máxima 863km/h: capacidade para 14 passageiros: Cor Azul
#
# - modelo Antonov An-2: velocidade máxima de 258 Km/h: capacidade para 12 passageiros: Cor Azul


class Aviao:
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade
        self.cor = "azul"

    def __str__(self):
        string = (
            f"O avião de modelo {self.modelo} "
            + f"possui uma velocidade máxima de {self.velocidade_maxima}, "
            + f"capacidade para {self.capacidade} passageiros e "
            + f"é da cor {self.cor}."
        )
        return string


a = Aviao("BOIENG456", "1500 km/h", 400)
b = Aviao("Embraer Praetor 600", "863 km/h", 14)
c = Aviao("Antonov An-2", "258 km/h", 12)

lista = [a, b, c]
for aviao in lista:
    print(aviao)
