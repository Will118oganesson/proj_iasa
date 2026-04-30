from .avaliador import Avaliador
from mod.estado import Estado
from lib.pee.melhor_prim.heuristica import Heuristica  # assuming this path

class AvaliadorHeur(Avaliador):
    def __init__(self, heuristica: Heuristica):
        self.heuristica = heuristica