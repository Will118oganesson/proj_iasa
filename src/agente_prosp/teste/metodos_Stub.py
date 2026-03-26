from sae.agente.movimento import Movimento
from lib.ecr.accao import Accao
from ecr.reaccao import Reaccao

class StubResposta:
    def ativar(self, percepcao, intensidade):
        from agente_prosp.accoes.mover import Mover
        return Mover(percepcao.direccao)  # always move in current direction

class StubEstimulo:
    def detectar(self, percepcao):
        return 1  # always triggers

class StubReaccao(Reaccao):
    def __init__(self):
        super().__init__(StubEstimulo(), StubResposta())