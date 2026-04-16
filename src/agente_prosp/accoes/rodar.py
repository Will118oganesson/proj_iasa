from sae import Movimento
from lib.ecr.accao import Accao

class Rodar(Accao):
    def __init__(self, direccao):
        super().__init__()
        self._movimento = Movimento(direccao, passo=0)

    @property
    def movimento(self):
        return self._movimento