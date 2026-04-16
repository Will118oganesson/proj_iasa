from lib.ecr.reaccao import Reaccao
from .estimulo_obs import EstimuloObst
from .resposta_evitar import RespostaEvitar

#comportamento evitar obstaculo nas varias direçao

class EvitarObst(Reaccao):
    def __init__(self):
        super().__init__(EstimuloObst(),RespostaEvitar())