from .procura_melhor_prim import ProcuraMelhorPrim

from mod.problema import Problema
from .heuristica import Heuristica
from pee.mec_proc.solucao import Solucao
from pee.mec_proc.no import No

class ProcuraInformada(ProcuraMelhorPrim):
    def procurar(self, problema: Problema, heuristica: Heuristica) -> Solucao:
        fronteira = self.fronteira  # or created internally depending on base class
        fronteira.iniciar()

        no_inicial = No(problema.estado_inicial())
        fronteira.inserir(no_inicial)

        while not fronteira.vazia:

            no = fronteira.remover()

            if problema.objectivo(no.estado):
                return Solucao(no)

            for operador in problema.operadores(no.estado):

                novo_estado = operador.aplicar(no.estado)

                novo_no = No(
                    estado=novo_estado,
                    operador=operador,
                    antecessor=no,
                    custo=no.custo + operador.custo()
                )

                # 🔥 THIS is where heuristic is used
                prioridade = heuristica.h(novo_estado)

                # depending on algorithm type (A*, Greedy, etc.)
                novo_no.prioridade = prioridade + novo_no.custo  # A*
                # or: novo_no.prioridade = prioridade           # Greedy

                if self._manter(novo_no):
                    fronteira.inserir(novo_no)

        return None