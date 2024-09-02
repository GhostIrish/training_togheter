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


# este é um exemplo de diferença, que no caso só retorna oque há de diferente em 'e' que não tem em 'f'.
conjunto_e = {1, 2, 3}
conjunto_f = {3, 4, 2}

print(conjunto_e.difference(conjunto_f))

# aqui retorna a diferença simétrica, ou seja, oque há de diferente em ambos os conjuntos.
conjunto_e = {1, 2, 3}
conjunto_f = {3, 4, 2}

print(conjunto_e.symmetric_difference(conjunto_f))


# Esse verifica se todos os elementos do conjunto 'a' estão presentes no conjunto 'b', caso estejam
# retorna True.
conjunto_a = {1, 2, 3}
conjunti_b = {4, 1, 2, 5, 6, 3}

print(conjunto_a.issubset(conjunti_b))
print(conjunto_b.issubset(conjunto_a))
# o método .issuperset é ao contrário, se os elementos de 'a' estivrem todos em 'b', retorna falso.

# o método .isdisjoint verifica se não ha nenhuma correlação entre os conjuntos, caso não tenha, 
# retornará True.

# o .add + valor desejado, adiciona um valor desejado ao conjunto

# o .clear() limpa os conjuntos e o .copy() faz uma copia

# o .discard(valor) descarta o valor desejado caso ele tenha no set

# o .pop() vai tirando os primeiros valores do conjunto cada vez que é chamado.