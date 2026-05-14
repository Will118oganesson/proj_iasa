from .procura_melhor_prim import ProcuraMelhorPrim

from mod.problema import Problema
from .heuristica import Heuristica
from pee.mec_proc.solucao import Solucao
from pee.mec_proc.no import No

class ProcuraInformada(ProcuraMelhorPrim):
    def __init__(self, avaliador):
            super().__init__(avaliador)

    def procurar(self, problema, heuristica):
          self.fronteira.avaliador._heuristica = heuristica
          return super().procurar(problema)
        


        