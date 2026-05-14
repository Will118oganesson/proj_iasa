from procura_profundidade import ProcuraProfundidade

from mod.problema import Problema
from pee.mec_proc.no import No

class ProcuraProfLim(ProcuraProfundidade):
    def __init__(self):
        super().__init__()
        self.__prof_max : int = 0

    def procurar(self, problema: Problema, prof_max: int=10):
        self.__prof_max = prof_max
        return super().procurar(problema)
    def _expandir(self, problema: Problema, no: No) -> list[No]:
        if no.profundidade >= self.__prof_max:
            return []
        return super()._expandir(problema, no)