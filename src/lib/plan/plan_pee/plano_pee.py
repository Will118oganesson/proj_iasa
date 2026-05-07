from sae.vistas.vista_amb import VistaAmb
from pee.mec_proc.solucao import Solucao
from mod.operador import Operador

class PlanoPEE:
    def __init__(self, solucao: Solucao):
        pass
    def obter_accao(self, estado) -> Operador:
        pass
    def mostrar(self, vista: VistaAmb):
        pass