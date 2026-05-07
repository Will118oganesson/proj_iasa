from mod.problema import Problema

from plan.modelo.modelo_plan import ModeloPlan
from mod.estado import Estado

class ProblemaPlan(Problema):
    def __init__(self, modelo_plan: ModeloPlan, estado_final: Estado):
        super().__init__(modelo_plan.obter_estado(), modelo_plan.obter_operadores())

    def objetivo(self, estado: Estado) -> bool:
        return estado == self._estado_final