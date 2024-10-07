# conta quantos valores aparecem em uma lista
def conta_valor_na_lista(lista, valor):
    contador = 0
    for elemento in lista:
        if elemento == valor:
            contador += 1
    return contador


# cria uma nova lista com os valores da lista original que aparecem mais de uma vez
def limita_repeticao(lista, limite):
  nova_lista = []
  for i in lista:
    if conta_valor_na_lista(nova_lista, i) < limite:
      nova_lista.append(i)
  return nova_lista


lista = [1, 2, 3, 1, 2, 1, 2, 3]

print(limita_repeticao(lista, 2))