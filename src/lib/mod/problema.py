from estado import Estado
from operador import Operador

class Problema:
    def __init__(self, estado_inicial: Estado, operadores: list[Operador]):
        raise NotImplementedError
    
    def objectivo(self, estado: Estado) -> bool:
        raise NotImplementedError