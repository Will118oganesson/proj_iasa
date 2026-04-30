from avaliador_heur import AvaliadorHeur

from pee.mec_proc.no import No

class AvaliadorSof(AvaliadorHeur):
    def prioridade(self, no: No) -> float:
        return self.heuristica.h(no.estado)