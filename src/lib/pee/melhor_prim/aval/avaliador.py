from abc import ABC, abstractmethod
from pee.mec_proc.no import No

class Avaliador(ABC):
    @abstractmethod
    def prioridade(self, no: No) -> float:
        pass