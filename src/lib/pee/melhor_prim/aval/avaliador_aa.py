from .avaliador_heur import AvaliadorHeur
from lib.pee.mec_proc.no import No

class AvaliadorAA(AvaliadorHeur):
    def prioridade(self, no: No) -> float: #double
        return no.custo + self.heuristica.h(no.estado)
        