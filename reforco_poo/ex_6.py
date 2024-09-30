from abc import property


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
    @property
    def preco_(self):
        return self.preco > 0
    
    @preco_.setter
    def preco_(self, value):
        if value > 0:
            self.preco = value
        else:
            raise ValueError('Preço inválido')