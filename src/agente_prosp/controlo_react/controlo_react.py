from ecr.accao import Accao
from lib.agente.Controlo import Controlo

class ControloReact(Controlo):

    def __init__(self, comportamento):
        self.__comportamento = comportamento
    
    def processar(self, percepcao):
        return self.__comportamento.activar(percepcao)