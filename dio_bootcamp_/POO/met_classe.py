# metodos de classe e metodos estaticos

# geralmente métodos de classe são usados para criar métodos de fábrica
# e 
# metodos estaticos normalmente são usados para criar funções utilitarias na classe.

# ex:

# class Pessoa:
#     def __init__(self, nome= None, idade= None):
#         self.nome = nome
#         self.idade = idade
    
#     def create_from_birth(self, ano, mes, dia, nome):
#         idade = 2024 - ano
#         return Pessoa(nome, idade)
    

# #criando normalmente
# p = Pessoa('Guilherme', 28)
# print(p.nome, p.idade)

# # chamando pelo método para definir a idade baseado no nascimento

# p2 = Pessoa().create_from_birth(2002, 12, 11, 'Hariel')
# print(p2.nome, p2.idade)
# O resultado sai correto mas fica estranho não, comentei tudo e vou mostrar como fazer usando metodos de classe

class Pessoa:
    def __init__(self, nome= None, idade= None):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def create_from_birth(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)
    @staticmethod
    def maioridade(idade):
        return idade >= 18

#criando normalmente
p = Pessoa('Guilherme', 28)
print(p.nome, p.idade)

# chamando pelo método para definir a idade baseado no nascimento

p2 = Pessoa.create_from_birth(2002, 12, 11, 'Hariel')
print(p2.nome, p2.idade)

print(Pessoa.maioridade(18))
print(Pessoa.maioridade(15))

# metodos estaticos basicamente atribuem funções para a classe que podem ser usados fora dela