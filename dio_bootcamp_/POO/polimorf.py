# polimorfismo
# É o conceito de que uma classe pode ter mais de uma forma de se comportar
# de acordo com o tipo de objeto que ela é instanciada.

# ex:
class Passaro:
  def voar(self): pass

class Papagaio(Passaro):
  def voar(self):
    print('Papagaio voando...')

class Pato(Passaro):
  def voar(self):
    print('Pato não voa...')

def plano_d_voo(passaro):
  passaro.voar()

plano_d_voo(Papagaio())
plano_d_voo(Pato())
# basicamente pelo oq entendi ao chamar plano de voo, ele vai chamar o metodo voar de acordo 
# com o objeto que foi passado, tipo, quando voce chama plano_d_voo da classe, ele aciona o voar
# de acordo com a classe.,

# por exemplo, a classe passaro tem o método voar, mas a classe papagaio e 
# pato tem suas próprias definições de voar, então ao chamar plano de voo, 
# ele vai chamar o metodo voar de acordo com o objeto que foi passado.