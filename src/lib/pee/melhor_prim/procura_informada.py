from procura_melhor_prim import ProcuraMelhorPrim

from mod.problema import Problema
from heuristica import Heuristica
from pee.mec_proc.solucao import Solucao

class ProcuraInformada(ProcuraMelhorPrim):
    def procurar(self, problema: Problema, heuristica: Heuristica) -> Solucao:
        return