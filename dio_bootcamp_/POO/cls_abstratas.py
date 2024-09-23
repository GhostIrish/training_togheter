# criando classes abstratas com o módulo ABC

from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass
    # essa classe não pode mais ser chamada diretamente por ter atributos abstratos
    # ou seja, as classes que herdarem essa classe controlremoto serão OBRIGADAS
    # a terum método ligar e desligar.
    
    @property
    @abstractmethod
    def marca(self):
        pass
    # agora é obrigatorio implementar a property 'marca', caso contrario o codigo nao funciona
    # IMPORTANTE!!!!: O property sozinho não garante a necessidade de implementar uma marcan oque da essa garantia
    # é o abstractmethod.
    
class ControleTV(ControleRemoto):
    def ligar(self):
        print('ligando a tv')
        print()
        print('Ligado!')
        
    def desligar(self):
        print('Desligando a TV...')
        print()
        print('Desligado!')

    @property
    def marca(self):
        return 'Philco'
    # se a classe não tivesse essas funções, ia disparar erro, tem que ter as TRÊS.
    # as classes que herdam a abstrata, não precisam por o abstractmethod, so o property
    
class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print('ligando o ar')
        print()
        print('Ligado!')
        
    def desligar(self):
        print('Desligando o ar...')
        print()
        print('Desligado!')
        
    @property
    def marca(self):
        return 'LG'
    
controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)