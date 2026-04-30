import heapq
from .no import No

class Fronteira:
    def __init__(self):
        self._dados = []
        self._contador = 0
        self.vazia = True

    def iniciar(self):
        self._dados.clear()
        self._contador = 0
        self.vazia = True

    def inserir(self, no: No):
        self._contador += 1
        heapq.heappush(self._dados, (no.prioridade, self._contador, no))
        self.vazia = False

    def remover(self) -> No:
        _, _, no = heapq.heappop(self._dados)
        self.vazia = len(self._dados) == 0
        return no