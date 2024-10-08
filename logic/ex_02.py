def is_pangram(st):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alpha_list = [n for n in alphabet]
    list_ = []
    
    for letters in st:
        letters = letters.upper()
        if letters in alphabet:
            list_.append(letters)
    
    print(list_)
    
    if alpha_list in list_:
        return True
    else:
        return False


print(is_pangram('The quick brown fox jumps over the lazy dog'))

# codigo corrigido

def is_pangram(st):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')  # Conjunto com todas as letras
    st = st.lower()  # Converte a string para minúsculas
    letters_in_string = set()  # Para armazenar as letras encontradas
    
    # Itera pela string e adiciona as letras no conjunto
    for letter in st:
        if letter.isalpha():  # Verifica se o caractere é uma letra
            letters_in_string.add(letter)
    
    # Verifica se o conjunto de letras da string contém todas as letras do alfabeto
    return letters_in_string >= alphabet

# Testando
print(is_pangram('The quick brown fox jumps over the lazy dog'))  # True
