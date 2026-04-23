from avaliador_heur import AvaliadorHeur
from mec_proc.no import No

class AvaliadorAA(AvaliadorHeur):
    def prioridade(self, no: No) -> float: #double
        raise NotImplementedError