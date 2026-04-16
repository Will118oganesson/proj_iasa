from lib.ecr.comportamento import Comportamento
from abc import abstractmethod

class ComportComp(Comportamento):
    def __init__(self, comportamentos):
        self.__comportamentos = comportamentos
        
    def activar(self, percepcao):
        accoes = []

        for comportamento in self.__comportamentos:
            accao = comportamento.activar(percepcao)
            if accao:
                accoes.append(accao)

        accoes_validas = []
        for accao in accoes:
            if accao is not None:
                accoes_validas.append(accao)
        
        if len(accoes_validas) == 0:
            return None

        if accoes:
            return self.seleccionar_accao(accoes_validas)
        
    @abstractmethod
    def seleccionar_accao(self, accoes):
        pass