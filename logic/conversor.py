# Desafio dos conversores
# Metro para Km
# Celsius para feireheight
# reais para dollar
from os import system
import requests

url_api = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'
response = requests.get(url_api)
data = response.json()
dolar = data['USDBRL']['bid']
dolar = float(dolar)

def clear_prompt():
  print()
  print("Press enter...")
  input()
  system("cls")

while True:
  menu = '''
  - CONVERSORES -
  [1] Metro para Km
  [2] ºC para ºF
  [3] Real para Dolar
  [4] Sair
  '''
  print(menu)
  print()
  try:
    option = int(input('Escolha uma opção: '))
    print()
    system("cls")
    if option == 1:
      sub_menu = '''
  [1] Metro para Km
  [2] Km para Metro
      '''
      print(sub_menu)
      option_sub = int(input('Escolha uma opção: '))
      print()
      
      if option_sub == 1:
        metro = float(input('Digite o valor em metros: '))
        print()
        print(f'{metro} metros equivale a {metro/1000} Km')
        clear_prompt()
        
      else:
        km = float(input('Digite o valor em Km: '))
        print()
        print(f'{km} Km equivale a {km*1000} metros')
        clear_prompt()

    elif option == 2:
      sub_menu = '''
  [1] ºC para ºF
  [2] ºF para ºC
      '''
      print(sub_menu)
      option_sub = int(input('Escolha uma opção: '))
      print()
      if option_sub == 1:
        celsius = float(input('Digite o valor em ºC: '))
        print()
        print(f'{celsius} ºC equivale a {(celsius * 9/5) + 32} ºF')
        clear_prompt()
        
      else:
        f = float(input('Digite o valor em ºF: '))
        print()
        print(f'{f} ºF equivale a {(f - 32) * 5/9} ºC')
        clear_prompt()
        
    elif option == 3:
      sub_menu = '''
  [1] Real para Dolar
  [2] Dolar para Real
      '''
      print(sub_menu)
      print()
      option_sub = int(input('Escolha uma opção: '))
      print()
      if option_sub == 1:
        real = float(input('Digite o valor em R$: '))
        print()
        print(f'{real} R$ equivale a {real/dolar:.2f} US$')
        clear_prompt()
      else:
        dolar_input = float(input('Digite o valor em US$: '))
        print()
        print(f'{dolar_input} US$ equivale a {dolar_input*dolar:.2f} R$')
        clear_prompt()
        
    elif option == 4:
      print('Saindo...')
      break
      
    else:
      print('Opção inválida')
      
  except ValueError:
    print("Value error")
    clear_prompt()