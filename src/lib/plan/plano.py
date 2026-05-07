from abc import ABC

from mod.estado import Estado
from mod.operador import Operador

from lib.sae.vistas.vista_amb import VistaAmb

class Plano(ABC):
    def obter_accao(self, estado: Estado) -> Operador:
        pass
    def mostrar(self, vista):
        pass