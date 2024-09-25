# Herança e Construtores
# Crie duas classes: Animal (superclasse) e Cachorro (subclasse). No Animal, implemente atributos como nome e idade, 
# e métodos como falar (um método genérico que retorna uma string). No Cachorro, sobrescreva o método falar para retornar "Au Au". 
# Crie uma instância de Cachorro e teste os métodos.

class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def falar(self):
        return 'O animal esta falando'

class Cachorro(Animal):
    def falar(self):
        return 'Au Au'
    
class Gato(Animal):
    pass
    
c1 = Cachorro('Cachorro', 5)

print(c1.falar())
print(c1.nome)
print(c1.idade)

g1 = Gato('Gato', 3)

print(g1.falar())
print(g1.nome)
print(g1.idade)