from agente.Accao import Accao

class AccaoJogo(Accao):

    def __init__(self, comando):
        self.__comando = comando
    
    def comando(self):
        return self.__comando