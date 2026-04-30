from pee.mec_proc.no import No
from pee.mec_proc.fronteira import Fronteira

class FronteiraLIFO(Fronteira):
    def inserir(self, no: No):
        self._dados.insert(0, no)
        self.vazia = False