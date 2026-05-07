import math
from pee.melhor_prim.heuristica import Heuristica

from mod.estado import Estado

class HeurDist(Heuristica):
    def __init__(self, estado_final: Estado):
        self._estado_final = estado_final
    
    def h(self, estado: Estado) -> int:
        return math.dist(self._estado.posicao, self._estado_final.posicao)