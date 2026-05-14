import heapq
from pee.mec_proc.fronteira import Fronteira
from pee.melhor_prim.aval.avaliador import Avaliador
from pee.mec_proc.no import No

class FronteiraPrioridade(Fronteira):
    def __init__(self, avaliador: Avaliador):
        super().__init__()
        self.avaliador = avaliador
        self._contador = 0

    def inserir(self, no: No):
        no.prioridade = self.avaliador.avaliar(no)
        self._contador += 1
        heapq.heappush(self._dados, (no.prioridade, self._contador, no))
        self.vazia = False
    
    def remover(self) -> No:
        _, _, no = heapq.heappop(self._dados)
        self.vazia = len(self._dados) == 0
        return no