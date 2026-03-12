from abc import ABC, abstractmethod

class Agente(ABC):
    
    def __init__(self, controlo):
        self.__controlo = controlo


        
    
    @abstractmethod
    def _percepcionar(self):
        """Percepcionar o ambiente - retorna Percepcao"""
        pass



    
    @abstractmethod
    def _actuar(self, accao):
        """Actuar no ambiente com a accao"""
        pass

    def _controlo(self):
        return self.__controlo

    
    def executar(self):
        percepcao = self._percepcionar()
        accao = self.__controlo.processar(percepcao)
        # if accao is not None:
            #self._actuar(accao)