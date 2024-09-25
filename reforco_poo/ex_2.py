from abc import ABC, abstractmethod

# Explicando de uma maneira simples, basicamente a classe abstrata fala assim 'As classes que herdam de mim tem que ter as suas proprias definições
# do que for definido aqui.'
class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Circulo(FormaGeometrica):
    def calcular_area(self, raio):
        return 3.14 * (raio**2)

class Quadrado(FormaGeometrica):
    def calcular_area(self, lado):
        return lado * lado


c1 = Circulo()
print(c1.calcular_area(2.5))

q1 = Quadrado()
print(q1.calcular_area(5))

# se chamar assim da erro, pq nao é possivel instanciar uma classe abstrata
# f1 = FormaGeometrica()

# a principal diferença entre ela e o property é que as classes abstratas são uma assinatura das classes que herdam dela
# no caso do exemplo é como se todas classes que são herdadas tivessem um 'calcular_area', mas não necessariamente precisam ser implementados
# na classe.

# ja o property te obriga a implementar essas definições, ou seja, o circulo ali não necessariamente precisa ter um calcular area, mas se fosse um property
# em forma geometrica, seria obrigatorio ter essa classe definida.