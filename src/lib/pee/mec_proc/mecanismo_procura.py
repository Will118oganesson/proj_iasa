from abc import ABC, abstractmethod


from .no import No
from .fronteira import Fronteira
from mod.problema import Problema
from .solucao import Solucao


class MecanismoProcura(ABC):

    def __init__(self, fronteira: Fronteira):
        self.fronteira = fronteira

    def _iniciar_memoria(self):
        pass

    def _memorizar(self, no: No):
        pass

    @abstractmethod
    def procurar(self, problema: Problema) -> Solucao:
        pass

    def _expandir(self, problema: Problema , no: No) -> list[No]:
        pass