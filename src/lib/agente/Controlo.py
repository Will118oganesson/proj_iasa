from abc import ABC, abstractmethod

class Controlo(ABC):
    
    @abstractmethod
    def processar(self, percepcao):
        """Processar percepcao e retornar accao"""
        pass