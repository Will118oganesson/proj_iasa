from procura_profundidade import ProcuraProfundidade

from mod.problema import Problema
from pee.mec_proc.no import No

class ProcuraProfLim(ProcuraProfundidade):
    __prof_max : int = 0

    def procurar(self, problema: Problema, prof_max: int=10):
        return
    def _expandir(self, problem: Problema, no: No) -> list[No]:
        return