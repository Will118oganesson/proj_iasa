from lib.ecr.comportamento import Comportamento
from abc import abstractmethod

class ComportComp(Comportamento):
    def __init__(self, comportamentos):
        self.__comportamentos = comportamentos
        
    def activar(self, percepcao):
        accoes = []

        for comportamento in self.__comportamentos:
            accao = comportamento.ativar(percepcao)
            if accao:
                accoes.append(accao)
        if accoes:
            return self.seleccionar_accao(accoes)
        
    @abstractmethod
    def seleccionar_accao(self, accoes):
        pass