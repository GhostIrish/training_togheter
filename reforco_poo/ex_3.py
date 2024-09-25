
class Funcionario:
    def __init__(self, nome, sobrenome, matricula):
        self.nome = nome
        self.sobrenome = sobrenome
        self.matricula = matricula
class Gerente(Funcionario):
    def __init__(self, nome, sobrenome, matricula, pl, plano_saude):
        super().__init__(nome, sobrenome, matricula)
        self.pl = pl
        self.plano_saude = plano_saude
    
    def calcular_salario(self):
        salario = 5000
        self.pl = 2500
        return (salario + self.pl)

class Assistente(Funcionario):
    def __init__(self, nome, sobrenome, matricula, plano_saude):
        super().__init__(nome, sobrenome, matricula)
        self.plano_saude = plano_saude
    
    def calcular_salario(self):
        return 2500

class Estagiario(Funcionario):
    def __init__(self, nome, sobrenome, matricula):
        super().__init__(nome, sobrenome, matricula)
        
    def calcular_salario(self):
        return 1200
    
def salario(valor):
    return valor.calcular_salario()

g1 = Gerente('hariel', 'lima', '123', 2500, 'sim')
a1 = Assistente('pedro', 'lima', '123', 'sim')
e1 = Estagiario('carlos', 'lima', '123')

print(salario(g1))
print(salario(a1))
print(salario(e1))