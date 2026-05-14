from pee.mec_proc.mecanismo_procura import MecanismoProcura
from pee.mec_proc.no import No
from mod.problema import Problema
from pee.mec_proc.solucao import Solucao

class ProcuraGrafo(MecanismoProcura):
    def __init__(self, fronteira):
        super().__init__(fronteira)
        self._visitados = set()      # memória de estados já expandidos
        self._nos_processados = 0

    def _iniciar_memoria(self):
        self.fronteira.iniciar()
        self._visitados.clear()
        self._nos_processados = 0

    def _memorizar(self, no: No):
        self.fronteira.inserir(no)

    def _manter(self, no: No) -> bool:
        """Um nó deve ser explorado se o seu estado ainda não foi visitado."""
        return no.estado.id_valor() not in self._visitados

    def procurar(self, problema: Problema) -> Solucao:
        self._iniciar_memoria()
        no = No(problema.estado_inicial)
        self._memorizar(no)

        while not self.fronteira.vazia:
            no = self.fronteira.remover()
            if problema.objectivo(no.estado):
                return Solucao(no)

            # Marca o estado como visitado agora que vai ser expandido
            self._visitados.add(no.estado.id_valor())
            self._nos_processados += 1

            for sucessor in self._expandir(problema, no):
                if self._manter(sucessor):
                    self._memorizar(sucessor)

        return None

    def _expandir(self, problema: Problema, no: No) -> list[No]:
        sucessores = []
        estado = no.estado
        for operador in problema.operadores:
            estado_suc = operador.aplicar(estado)
            if estado_suc is not None:
                custo = no.custo + operador.custo(estado, estado_suc)
                no_suc = No(estado_suc, operador, no, custo)
                sucessores.append(no_suc)
        return sucessores