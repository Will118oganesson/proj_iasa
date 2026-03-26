from ecr.accao import Accao

class ControloReact:

    def __init__(self, comportamento):
        self.__comportamento = comportamento
    
    def processar(self, percepcao) -> Accao:
        return self.__comportamento.activar(percepcao)