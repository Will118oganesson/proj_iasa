from abc import ABC, abstractmethod
from ecr.accao import Accao

class Comportamento(ABC):
    @abstractmethod
    def activar(self, percepcao):
        raise NotImplemented