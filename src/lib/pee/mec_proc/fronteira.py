import heapq
from .no import No

class Fronteira:
    def __init__(self):
        self._nos = []
        self.iniciar()

    @property
    def vazia(self):
        return len(self._nos) == 0
    
    def iniciar(self):
        self._nos.clear()


    def inserir(self, no: No):
        self._nos.append(no)

    def remover(self) -> No:
        return self._nos.pop(0)
        
    def tamanho(self) -> int:
        return len(self._nos)