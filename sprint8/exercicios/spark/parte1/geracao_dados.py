import csv
import random
import time
import names

# Etapa 1 --------------------------------

lista = [random.randint(1, 1000) for i in range(250)]
lista.reverse()
print(lista)
print("-"*20)

# Etapa 2 --------------------------------

animais = ["pinguim",
           "aguia",
           "crocodilo",
           "jaguar",
           "camelo",
           "baleia",
           "polvo",
           "gavião",
           "ornitorrinco",
           "guaxinim",
           "texugo",
           "alpaca",
           "búfalo",
           "caranguejo",
           "doninha",
           "falcão",
           "flamingo",
           "galo",
           "hiena",
           "iguana"
           ]

animais.sort()
[print(i) for i in animais]
print("-"*20)

animais_dict = [{"nome": animal} for animal in animais]

with open('animais.csv', 'w', newline='') as arquivo_csv:
    campos = ['nome']
    writer = csv.DictWriter(arquivo_csv, fieldnames=campos)
    writer.writeheader()
    writer.writerows(animais_dict)

# Etapa 3 --------------------------------

random.seed(40)
qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

aux = [names.get_full_name() for _ in range(0,qtd_nomes_unicos)]

print(f"Gerando {qtd_nomes_aleatorios} nomes aleatórios...")

dados = [random.choice(aux) for _ in range(0,qtd_nomes_aleatorios)]

with open('nomes_aleatorios.txt','w') as f:
    for nome in dados:
        f.write(f"{nome}\n")

print(f"Nomes gerados.")
