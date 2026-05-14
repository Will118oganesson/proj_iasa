from .estado import Estado
from .operador import Operador

class Problema:
    def __init__(self, estado_inicial: Estado, operadores: list):
        self.estado_inicial = estado_inicial
        self.operadores = operadores

    def objectivo(self, estado: Estado) -> bool:
        raise NotImplementedError("Subclasses devem implementar objectivo()")