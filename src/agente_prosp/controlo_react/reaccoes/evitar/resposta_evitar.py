from lib.ecr.resposta import Resposta
from agente_prosp.accoes.rodar import Rodar

class RespostaEvitar(Resposta):
    def __init__(self):
        #super().__init__(Rodar(None))
        super().__init__()

    def _obter_accao(self, percepcao):
        novaDir = percepcao.direccao.rodar(1)
        self._accao = Rodar(novaDir)
        return self._accao

#resposta para evitar o obstaculo tem a funcao obter_accao, para gerar nova accao e rotacao na direcao do agente