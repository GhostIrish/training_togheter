class Cachorro():
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def latir(self):
        print(f'O cachorro {self.nome} está latindo')
    
class Pug(Cachorro):
    def dormir(self):
        self.acordado = False
        print(self.acordado)
        print(f'O cachorro pug {self.nome} agora está dormindo.')

class Pitbull(Cachorro):
    def latido(self):
        print(f'O pitbull {self.nome} ta bolado.')
       
c = Pug('Bruto', 'marrom')

p = Pitbull('Rex', 'marrom')

c.dormir()

print()
p.latido()
