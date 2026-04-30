from mod.estado import Estado
from abc import ABC, abstractmethod

class Heuristica(ABC):
    @abstractmethod
    def h(self, estado: Estado) -> float:
        pass