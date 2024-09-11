class Cachorro():
    def __init__(self, nome, cor, acordado=True):
        print('Dando inicio a classe')
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def latir(self):
        print(f'O cachorro {self.nome} está latindo')
    
c = Cachorro('Pug', 'marrom')

c.latir()