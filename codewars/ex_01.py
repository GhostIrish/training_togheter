# ex 01: Crie um programa que solicite uma frase ao usuário e conte o número de palavras, letras e espaços na frase. 

def verifica_string(string: str):
    string = string.strip().upper()
    palavras = 0
    letras = 0
    espaco = 0
    separando = string.split()
    for letra in string:
        if letra in ' ':
            espaco += 1
        if letra in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            letras += 1
    for palavra in separando:
        if len(palavra) > 1:
            palavras += 1

    return f'A frase "{string.capitalize()}", tem um total de {palavras} palavras, {letras} letras e {espaco} espaços.'

frase = str(input('Digite uma frase: '))


print(verifica_string(frase))