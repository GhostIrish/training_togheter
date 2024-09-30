
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def andar(self):
        print(f"O carro {self.marca} {self.modelo} está andando.")

class Pessoa:
    def __init__(self, nome, idade, carro=None):
        self.nome = nome
        self.idade = idade
        self.carro = carro

    def dirigir(self):
        if self.carro:
            print(f'{self.nome} esta dirigindo.')
        
        else:
            print(f'{self.nome} não possui um carro.')
            
# Criando uma instância de Carro
meu_carro = Carro("Toyota", "Corolla")

# Criando uma instância de Pessoa com o carro
pessoa = Pessoa("João", 20, meu_carro)

# Fazendo a pessoa dirigir o carro
pessoa.dirigir()