from agente.Percepcao import Percepcao

class PercecaoJogo(Percepcao):

    def __init__(self, evento):
        self.__evento = evento
    
    def evento(self):
        return self.__evento