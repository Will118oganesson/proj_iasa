from mod.operador import Operador
from lib.agente.Accao import Accao 
from sae import Direccao
from mod.estado import Estado

class OperadorMover(Operador):
    ang:float = 0
    accao:Accao = None

    def __init__(self, modelo_mundo, direccao: Direccao):
        pass

    def aplicar(self, estado:Estado) -> Estado:
        pass

    def custo(self, estado: Estado, estado_suc: Estado) -> float:
        pass