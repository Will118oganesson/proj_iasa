from abc import ABC, abstractmethod
from .no import No
from .fronteira import Fronteira
from mod.problema import Problema
from .solucao import Solucao

class MecanismoProcura(ABC):

    def __init__(self, fronteira: Fronteira):
        self.fronteira = fronteira
        self._nos_processados = 0

    @property
    def nos_processados(self):
        return self._nos_processados

    @property
    def nos_memoria(self):
        """Número de nós actualmente na fronteira (em memória)."""
        return self.fronteira.tamanho()  

    def _iniciar_memoria(self):
        self.fronteira.iniciar()
        self._nos_processados = 0

    def _memorizar(self, no: No):
        self.fronteira.inserir(no)

    @abstractmethod
    def procurar(self, problema: Problema) -> Solucao:
        
        self._iniciar_memoria()
        no = No(problema.estado_inicial)
        self._memorizar(no)

        while not self.fronteira.vazia:
            no = self.fronteira.remover()
            if problema.objectivo(no.estado):
                return Solucao(no)

            for sucessor in self._expandir(problema, no):
                self._memorizar(sucessor)

            self._nos_processados += 1

        return None

    def _expandir(self, problema: Problema, no: No) -> list[No]:
        sucessores = []
        estado = no.estado
        for operador in problema.operadores:
            estado_suc = operador.aplicar(estado)
            if estado_suc is not None:
                custo = no.custo + operador.custo(estado, estado_suc)
                no_suc = No(estado_suc, operador, no, custo, no.profundidade + 1)
                sucessores.append(no_suc)
        return sucessores