from pee.mec_proc.no import No
from pee.mec_proc.fronteira import Fronteira

class FronteiraFIFO(Fronteira):
    def inserir(self, no: No):
        return