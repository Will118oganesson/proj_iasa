from procura_prof_lim import ProcuraProfLim
from mod.problema import Problema

class ProcuraProfIter(ProcuraProfLim):
    def procurar(self, problema: Problema, inc_prof: int = 1, limite_prof : int = 100):
        raise NotImplementedError