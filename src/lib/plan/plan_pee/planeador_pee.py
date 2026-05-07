from pee.melhor_prim.procura_aa import ProcuraAA as MecanismoPEE

from plan.plan_pee.mod_prob.heur_dist import HeurDist
from plan.plan_pee.plano_pee import PlanoPEE
from plan.planeador import Planeador
from .mod_prob.problema_plan import ProblemaPlan

from mod.estado import Estado
from plan.modelo.modelo_plan import ModeloPlan

class PlaneadorPEE(Planeador):
    def __init__(self):
        self.__mec_pee = MecanismoPEE()

    def planear(self, modelo_plan: ModeloPlan, objetivos: list[Estado]) -> PlanoPEE:
        estado_final = objetivos[0]
        problema = ProblemaPlan(modelo_plan, estado_final)
        heuristica = HeurDist(estado_final)
        solucao = self.__mec_pee.procurar(problema, heuristica)
        return PlanoPEE(solucao)