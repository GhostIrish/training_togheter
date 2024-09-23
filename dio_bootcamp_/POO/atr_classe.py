# atributos do objeto

# ex:
class Estudante:
  escola = 'Dio'

  def __init__(self, nome, numero):
    self.nome = nome
    self.numero = numero

  def __str__(self):
    return f'{self.nome}  ({self.numero} - {self.escola})'

gui = Estudante('Gui', 165413)
gi = Estudante('Gi', 165789)

# Estudante.escola = 'Nova escola'

print(gui)
print()
print(gi)

# variaveis de instancia são variaveis unicas por objeto, exemplo, se eu trocar o numero da matricula de um estudante
# vai trocar somente o numero da matricula dele.
# mas se eu trocar a variável da classe, que no caso do ex é o 'Dio', ele vai trocar para todos os outros 
# objetos também.

