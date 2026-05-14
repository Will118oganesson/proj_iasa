from pee.mec_proc.fronteira import Fronteira
from pee.mec_proc.no import No

class FronteiraFIFO(Fronteira):
    def __init__(self):
        super().__init__()
        self._nos = []

    @property
    def vazia(self):
        return len(self._nos) == 0

    def iniciar(self):
        self._nos.clear()
        self.vazia = True   # mantém a propriedade herdada, se necessário

    def inserir(self, no: No):
        self._nos.append(no)

    def remover(self) -> No:
        return self._nos.pop(0)