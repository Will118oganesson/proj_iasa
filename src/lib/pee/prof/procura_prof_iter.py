from procura_prof_lim import ProcuraProfLim
from mod.problema import Problema

class ProcuraProfIter(ProcuraProfLim):
    def procurar(self, problema: Problema, inc_prof: int = 1, limite_prof : int = 100):
        for limite in range(inc_prof, limite_prof + 1, inc_prof):
            solucao = super().procurar(problema, prof_max=limite)
            if solucao is not None:
                return solucao
        return None