from pee.mec_proc.mecanismo_procura import MecanismoProcura
from pee.prof.fronteira_lifo import FronteiraLIFO

class ProcuraProfundidade(MecanismoProcura):
    def __init__(self):
        super().__init__(FronteiraLIFO())