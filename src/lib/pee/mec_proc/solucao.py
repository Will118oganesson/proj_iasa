from .no import No
from .passo_solucao import PassoSolucao

class Solucao:
    def __init__(self, no_final: No):
        self.__no_final = no_final

    def percurso(self):
        caminho = []
        no = self.__no_final
        while no.antecessor is not None:
            caminho.append(no.operador)
            no = no.antecessor
        caminho.reverse()
        return caminho

    def obter_passos(self):
        passos = []
        no = self.__no_final
        while no.antecessor is not None:
            passos.append(PassoSolucao(no.estado, no.operador))
            no = no.antecessor
        passos.reverse()
        return passos

    def dimensao(self) -> int:
        return len(self.obter_passos())

    def custo(self) -> float:
        return self.__no_final.custo if self.__no_final else 0.0