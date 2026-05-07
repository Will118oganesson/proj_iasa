from abc import ABC, abstractmethod
from lib.mod.estado import Estado
from lib.mod.operador import Operador

class ModeloPlan(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def obter_estado(self) -> Estado:
        pass

    @abstractmethod
    def obter_estados(self) -> list[Estado]:
        pass

    @abstractmethod
    def obter_operadores(self) -> list[Operador]:
        pass