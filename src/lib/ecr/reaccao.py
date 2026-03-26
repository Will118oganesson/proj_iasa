from ecr.accao import Accao

#
class Reaccao:
    def __init__(self, estimulo, resposta):
        self.__estimulo = estimulo
        self.__resposta = resposta

    def activar(self, percepcao) -> Accao:
        intensidade = self.estimulo.detectar(percepcao)

        if intensidade > 0:
            return self.resposta.ativar(percepcao, intensidade)