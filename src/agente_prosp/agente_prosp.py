import sae.agente.transdutor
from sae.agente.movimento import Movimento
from lib.agente import Agente

class AgenteProsp:
    def __init__(self, controlo):
        self.__controlo = controlo

    def executar(self):
        self.percepcionar()

    def percepcionar(self):
        percepcao = sae.transdutor.percepcionar()
        
        direcao_desejada = self.pensar(percepcao)

        movimento = Movimento(direcao_desejada, passo=1)
        sae.transdutor.actuar(movimento)

    def pensar(self, percepcao):
        return sae.ambiente.direccao.Direccao.NORTE