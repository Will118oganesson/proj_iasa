from aval.avaliador import Avaliador
from mec_proc.no import No

class AvaliadorCustoUnif(Avaliador):
    def prioridade(self, no: No) -> float: #double
        return no.custo