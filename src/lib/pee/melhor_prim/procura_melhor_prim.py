from ..mec_proc.mecanismo_procura import MecanismoProcura
from pee.melhor_prim.fronteira_prioridade import FronteiraPrioridade
from ..mec_proc.no import No
from ..mec_proc.solucao import Solucao

class ProcuraMelhorPrim(MecanismoProcura):
    def __init__(self, avaliador):
        fronteira = FronteiraPrioridade(avaliador)
        super().__init__(fronteira)

    def procurar(self, problema):
        self.fronteira.iniciar()
        no_inicial = No(problema.estado_inicial, None, None, 0.0)
        self.fronteira.inserir(no_inicial)
        visitados = set()

        while not self.fronteira.vazia:
            no = self.fronteira.remover()
            if problema.objectivo(no.estado):
                return Solucao(no)
            if no.estado.id_valor() in visitados:
                continue
            visitados.add(no.estado.id_valor())
            for operador in problema.operadores:
                novo_estado = operador.aplicar(no.estado)
                if novo_estado is None:
                    continue
                custo = no.custo + operador.custo(no.estado, novo_estado)
                novo_no = No(novo_estado, operador, no, custo)
                self.fronteira.inserir(novo_no)
        return None