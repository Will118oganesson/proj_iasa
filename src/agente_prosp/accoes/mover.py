from sae import Movimento
from lib.ecr.accao import Accao

class Mover(Accao):
    def __init__(self, direccao):
        super().__init__()
        self._movimento = Movimento(direccao)

    @property
    def movimento(self):
        return self._movimento

    