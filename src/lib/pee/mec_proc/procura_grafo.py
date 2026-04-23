from mecanismo_procura import MecanismoProcura
from no import No

class ProcuraGrafo(MecanismoProcura):
    def _iniciar_memoria(self):
        raise NotImplementedError
    def _memorizar(self, no: No):
        raise NotImplementedError
    def _manter(self, no:No) -> bool:
        raise NotImplemented