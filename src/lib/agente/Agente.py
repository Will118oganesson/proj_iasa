from abc import ABC, abstractmethod

class Agente(ABC):
    
    def _init_(self, controlo):
        self.__controlo = controlo


        
    
    @abstractmethod
    def _percepcionar(self):
        """Percepcionar o ambiente - retorna Percepcao"""
        pass



    
    @abstractmethod
    def _actuar(self, accao):
        """Actuar no ambiente com a accao"""
        pass



    
    def executar(self):
        pass