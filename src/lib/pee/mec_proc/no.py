from mod.estado import Estado
from mod.operador import Operador

class No:
    profundidade : int = 0
    custo : float = 0 #double
    prioridade : int = 0

    #def __init__(self, estado: Estado, operador: Operador, antecessor: No, custo: float):
    def __init__(self, estado: Estado, operador=None, antecessor=None, custo=0):
        self.estado = estado
        self.operador = operador
        self.antecessor = antecessor
        self.custo = custo