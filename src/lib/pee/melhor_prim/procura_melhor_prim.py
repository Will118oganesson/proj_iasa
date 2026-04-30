from .aval.avaliador import Avaliador
from pee.mec_proc.no import No

class ProcuraMelhorPrim:
    def __init__(self, avaliador: Avaliador):
        self.avaliador = avaliador
    def _manter(self, no: No) -> bool:
         return True