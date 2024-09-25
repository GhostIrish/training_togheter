class Banco:
    _total_clientes = 0  # Atributo de classe (compartilhado por todas as instâncias)
    
    @classmethod
    def total_clientes(cls):
        return cls._total_clientes  # Método de classe para retornar o total de clientes
    
    @classmethod
    def incrementar_clientes(cls):
        cls._total_clientes += 1  # Método de classe para incrementar o número de clientes

class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.contas = []
        Banco.incrementar_clientes()  # Incrementa o total de clientes no banco ao criar um cliente
        
# Criando instâncias de Cliente
c1 = Cliente('John', 'Doe', '12345678901')
c2 = Cliente('Jane', 'Smith', '98765432109')
c3 = Cliente('Bob', 'Johnson', '10987654321')

# Verificando o total de clientes no banco
print(Banco.total_clientes())  # Saída: 3

# to com um pouco de dificuldades ainda, mas pelo oq entendi ate agora, isso serve pra voce poder usar atributos de classe
# entre os métodos para poder realizar operações, no exemplo ali, utilizamos o contador que começa em zero para que na func de incrementar
# seja acrescentado 1 a cada vez que um novo cliente é criado.