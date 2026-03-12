from agente.Accao import Accao
from ambiente.ComandoJogo import ComandoJogo

class AccaoJogo(Accao):

    def __init__(self, comando: ComandoJogo):
        self.__comando = comando
    
    def comando(self):
        return self.__comando