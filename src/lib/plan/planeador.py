#classe para carregar interface na qual ha metodo de abstracao e ha uma funcao planear q recebe self, modelo, plano e objetivos

from plan.modelo.modelo_plan import ModeloPlan
from mod.estado import Estado
from .plano import Plano

class Planeador:
    def __init__(self):
        return
    def planear(self, modelo_plan: ModeloPlan, objectivos: list[Estado]) -> Plano:
        pass