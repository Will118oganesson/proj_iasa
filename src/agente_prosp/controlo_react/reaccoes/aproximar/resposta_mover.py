
##mover numa direçao especifica ou na direçao atual caso a direçao nao foi indicada

from lib.ecr.resposta import Resposta
from agente_prosp.accoes.mover import Mover

class RespostaMover(Resposta):
    def __init__(self, direccao=None):
        super().__init__(Mover(direccao))