from agente.Percepcao import Percepcao
from ambiente.EventoJogo import EventoJogo

class PercecaoJogo(Percepcao):

    def __init__(self, evento: EventoJogo):
        self.__evento = evento
    
    def evento(self):
        return self.__evento