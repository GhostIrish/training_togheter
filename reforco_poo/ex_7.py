from abc import ABC, abstractmethod
import math

class Calculadora(ABC):
    @staticmethod
    @abstractmethod
    def somar(value_1, value_2):
        pass  # Método abstrato, precisa ser implementado na classe filha
    
    @staticmethod
    def subtrair(value_1, value_2):
        return value_1 - value_2
    
    @staticmethod
    def multiplicar(value_1, value_2):
        return value_1 * value_2
    
    @staticmethod
    def dividir(value_1, value_2):
        if value_2 != 0:
            return value_1 / value_2
        else:
            raise ValueError("Não é possível dividir por zero.")

class CalculadoraCientifica(Calculadora):
    @staticmethod
    def somar(value_1, value_2):
        return value_1 + value_2
    
    @staticmethod
    def logaritmo(value):
        if value > 0:
            return math.log(value)
        else:
            raise ValueError("O logaritmo só pode ser calculado para números positivos.")

# Exemplo de uso:
calculadora = CalculadoraCientifica()

# Testando as operações
print(calculadora.somar(3, 4))          # 7
print(calculadora.subtrair(10, 5))      # 5
print(calculadora.multiplicar(6, 3))    # 18
print(calculadora.dividir(10, 2))       # 5.0
print(calculadora.logaritmo(10))        # 2.302585092994046
