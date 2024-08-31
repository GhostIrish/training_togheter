import tweepy as tw
from twitter_api_keys import *


auth = tw.Client(bearer_token=bearer_key, consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=acess_token, access_token_secret=acess_token_secret)

# Nome do arquivo que armazenará o contador
contador_arquivo = "contador.txt"

# Tenta abrir o arquivo e ler o contador
try:
    with open(contador_arquivo, "r") as file:
        contador = int(file.read())
except FileNotFoundError:
    # Se o arquivo não existir, o contador começa em 0
    contador = 0

# Incrementa o contador
contador += 1

# Salva o novo valor de volta no arquivo
with open(contador_arquivo, "w") as file:
    file.write(str(contador))

tweet = f'Training my skills for {contador} days.'

try:
    response = auth.create_tweet(text=tweet)
    print('Sucessfully to tweet!')
    
except tw.errors.TooManyRequests as e:
    print("Excedeu o limite de requisições. Tente novamente mais tarde.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")