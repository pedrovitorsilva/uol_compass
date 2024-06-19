import hashlib

while True:

    print("-"*30)
    
    texto = input('Digite um texto: ')
    resultado = hashlib.sha1(texto.encode())

    print(f"\nO hash equivalente em SHA1 é : {resultado.hexdigest()}")
