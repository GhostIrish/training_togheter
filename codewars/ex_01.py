# exercicio basicamente consiste em fazer um verificador de senha que atinga os seguintes critérios:
# - seis digitos de caracteres
# - pelo menos um lowercase
# - pelo menos um uppercase
# - contenha pelo menos um digito
# - somente alphanumericos

def verificador_senhas(senha):
    if len(senha) < 6:
        print('Senha inválida, a senha deve conter pelo menos 6 digitos')
    
    for letter in senha:
        if letter.islower():
            break
        else:
            print('Senha inválida, a senha deve conter pelo menos um caractere minusculo(lowercase)')
            
    for letter in senha:
        if letter.isupper():
            break
        else:
            print('Senha inválida, a senha deve conter pelo menos um caractere maiusculo(uppercase)')

    for letter in senha:
        if letter.isnumeric():
            break
        else:
            print('Senha inválida, a senha deve conter pelo menos um numero')

    for letter in senha:
        if letter.isalnum():
            print('Senha inválida, não pode conter caracteres alfanumericos')
