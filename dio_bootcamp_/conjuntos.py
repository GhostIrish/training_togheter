# Relembrando set e conjuntos.

numeros = {1, 2, 3, 4} # set()
carros = ['gol', 'ford', 'gol', 'chevrolet']
carros = set(carros)

for n in numeros:
    if n == 1:
        print(n)
        
# ou

numeros = list(numeros)

print(numeros[0])


# um for com enumerate também resolve
carros = list(carros)

print(carros)
print(carros[2])

# Métodos da classe Set.
conjunto_a = {1, 2}
conjunto_b = {3, 4}

# ele retorna a interseção dos sets, ou seja, os valores juntos de ambos
print(conjunto_a.union(conjunto_b))


# este é um exemplo de interseção, só é mostrado oque está presente em ambos os conjuntos.
conjunto_c = {1, 2, 3}
conjunto_d = {3, 4, 2}

print(conjunto_c.intersection(conjunto_d))