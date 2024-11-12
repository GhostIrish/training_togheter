
def fatorial(num):
    if num < 0:
        raise ValueError('number must be non-negative')  # Corrigido para levantar o erro
    if num == 0:
        return 1
    
    resultado = 1
    while num > 1:
        resultado *= num
        num -= 1
        
# Testando a função

print(fatorial(5))  # 120
print(fatorial(10)) # 3628800
print(fatorial(0))  # 1
print(fatorial(-5)) # ValueError: n must be non-negative