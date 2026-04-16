from lib.ecr.reaccao import Reaccao
from .estimulo_alvo import EstimuloAlvo
from .resposta_mover import RespostaMover

class AproximarDir(Reaccao):
    #comportamento aproximar alvo numa direçao especifica
    def __init__(self, direccao):
        super().__init__(
            EstimuloAlvo(direccao),
            RespostaMover(direccao)
        )
    pass