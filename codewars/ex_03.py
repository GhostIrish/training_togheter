

def conta_palavras(lista):
    dic = {}
    cont = 0
    for palavra in lista:
        if palavra in dic:
            dic[palavra] += 1
        else:
            dic[palavra] = 1
        cont += 1
    for k, v in dic.items():
        print(f'A palavra {k} aparece {v} vezes nessa lista.')    
        print()


lista = ['a', 'b', 'c', 'd', 'maçã', 'maçã', 'manga']
conta_palavras(lista)