
class Carro:
    pass

class Pessoa:
    def __init__(self, nome, idade, carro: Carro):
        self.nome = nome
        self.idade = idade
        self.carro = Carro

    def dirigir(self):
        ...
