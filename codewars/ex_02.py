# ex 02: Peça ao usuário para inserir uma série de números, um de cada vez, até ele digitar "fim". 
# Armazene esses números em uma lista e, ao final, exiba o maior, o menor e a média dos números.
from os import system

valores = []

while True:
    print('Digite "fim" para parar.')
    numero = str(input('Digite um numero: ')).upper()
    system('cls')
    if numero == 'FIM':
        media = sum(valores) / len(valores)
        print(f'O maior valor é {max(valores)}')
        print(f'O menor valor é {min(valores)}')
        print(f'A média de valores é {media}')
        break
    else:
        try:
            numero = int(numero)
            valores.append(numero)
        except ValueError:
            print('O valor digitado não é um número.')
            
