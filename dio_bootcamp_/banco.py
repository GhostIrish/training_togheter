# versão 1.0 de um banco simples feito para o bootcamp da Dio

from os import system
from datetime import datetime

saldo = 0
limite = 500
ext_deposito = []
ext_saque = []
numero_d_transf = 1
LIMITE_TRANSF = 10

def limpa_prompt():
    print()
    print('Aperte enter para continuar.')
    input()
    system('cls')

def deposito(valor) -> float: 
    global saldo, ext_deposito, numero_d_transf
    global ext_deposito
    try:
        if numero_d_transf > LIMITE_TRANSF:
            print('O limite de transações diária foi excedido, por favor tente novamente amanhã.')
            
        else:     
            if valor > 0:
                data = datetime.now()
                # formate do jeito que precisar data.strftime("%d/%m/%Y %H:%M")
                # se tiver dificuldade no extrato, voltar aqui !!!!!
                registro_conta = [valor, saldo, data.strftime("%d/%m/%Y %H:%M")]
                numero_d_transf += 1
                saldo += valor
                ext_deposito.append(registro_conta)
                print('Depósito realizado com sucesso!')
                print(f'Seu depósito foi de R${valor:.2f} reais às {data.strftime("%H:%M")} do dia {data.strftime("%d/%m/%Y")}.')
                print(f'Seu saldo atualmente está em R${saldo:.2f} reais.')

            else:
                print('Valor inválido, O depósito deve ser maior que R$0.')
    except ValueError:
        print('Entrada inválida. Por favor, insira um valor numérico.')
    
def saque(valor) -> float:
    global numero_d_transf, saldo, limite

    try:
        # verifica se o saldo atual é igual a zero.
        if saldo == 0:
            print('O saldo atual é igual a zero.')
        else:
            # verifica se o valor a ser sacado é maior que zero
            if valor > 0:
                # verifica se o limite diario de transações foi atingido
                if numero_d_transf > LIMITE_TRANSF:
                    print('O limite de transações diária foi excedido, por favor tente novamente amanhã.')
                else:
                    # verifica se o valor a ser sacado atinge o limite de saque por vez, no exercicio em questão o limite é 500.
                    if valor > limite:
                        print('O limite de saque é de no máximo R$500 reais, por favor, tente novamente com um valor menor.')
                    else:
                        # verifica se o saldo é maior que zero
                        if saldo > 0 and valor <= saldo:
                            data = datetime.now()
                            numero_d_transf += 1
                            registro_conta = [valor, saldo, data.strftime("%d/%m/%Y %H:%M")]
                            saldo -= valor
                            ext_saque.append(registro_conta)
                            print(f'Você realizou um saque de R${valor:.2f} reais, \nseu saldo atual agora é de R${saldo:.2f}')
                        else:
                            print(f'Valor não disponível, seu saldo é de R${saldo:.2f} reais.')

            else:
                print('O valor mínimo de saque deve ser maior que R$0 reais.')
    except ValueError:
        print('Erro ocorrido durante o processo, tente novamente.')

def extrato():
    global saldo
    print()
    # verifica se houve algum deposito ou saque na conta
    if len(ext_deposito) == 0 and len(ext_saque) == 0:
        print('Não há historico de depósito e extrato atualmente.')

    else:
        print(f'Saldo atual: {saldo}')
        print()
        # itera sobre a lista de listas, desempacotando ela para utilizar separadamente os valores.
        print('---Histórico de Depósitos---')
        print('-------------------------')
        for lista in ext_deposito:
            val_1, val_2, val_3 = lista
            print(f'Valor depositado: R${val_1:.2f}')
            print(f'Saldo antes do depósito: R${val_2:.2f}')
            print(f'Data do depósito: {val_3}')
            print('-------------------------')
            
        print()
        print('---Histórico de Saques---')
        print('-------------------------')
        for lista in ext_saque:
            val_1, val_2, val_3 = lista
            print(f'Valor sacado: R${val_1:.2f}')
            print(f'Saldo antes do saque: R${val_2:.2f}')
            print(f'Data do saque: {val_3}')
            print('-------------------------')
        
    
menu = '''---Banquin---
[d] Depositar
[s] Sacar
[e] Extrato
[q] Exit
'''

while True:
    print(menu)
    opcao = str(input('Opção-> ')).strip().upper()
    try:
        if opcao == 'D':
            print('deposito')
            limpa_prompt()
            print('---Opção depósito---')
            valor = float(input('Valor a ser depositado: '))
            deposito(valor)
            limpa_prompt()
            
        elif opcao == 'S':
            print('sacar')
            limpa_prompt()
            print('---Opção de Saque---')
            print('Aviso: São permitidos apenas 3 saques diários com limite de R$500 reais.')
            print()
            valor = float(input('Valor a ser sacado: '))
            saque(valor)
            limpa_prompt()
            
        elif opcao == 'E':
            print('extrato')
            extrato()
            limpa_prompt()
            
        elif opcao == 'Q':
            break
        
        else:
            print('Opção inválida.')
            limpa_prompt()
    except ValueError:
        print('Erro ocorrido durante o processo, tente novamente.')
        
# amanhã é so mexer na logica de passar dos 3 saques diarios que ele ta passando e mandar pro dio
# pq de resto ta tudo certo