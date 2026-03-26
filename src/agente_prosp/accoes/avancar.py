from sae import Movimento
from lib.ecr.accao import Accao

class Avancar(Accao):
    def __init__(self):
        super().__init__()
        self._movimento = Movimento(None)  # mantém direção atual

    @property
    def movimento(self):
        return self._movimento