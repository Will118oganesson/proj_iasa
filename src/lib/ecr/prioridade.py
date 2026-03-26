from .comportComp import ComportComp

class Prioridade(ComportComp):
    def seleccionar_accao(self, accoes):
        return max(accoes, key=lambda a: a.prioridade, default=None)


       