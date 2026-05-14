import math
from mod.operador import Operador
from agente_prosp.accoes.mover import Mover
from lib.agente.Accao import Accao
from sae import Direccao
from mod.estado import Estado

class OperadorMover(Operador):
    def __init__(self, modelo_mundo, direccao: Direccao):
        self.__modelo_mundo = modelo_mundo
        # Inverte o sinal do ângulo para converter de matemático (Y↑) para ecrã (Y↓)
        self.ang = -direccao.value
        self.__accao = Mover(direccao)   # a acção continua a usar a direcção original

    @property
    def angulo(self):
        return self.ang

    @property
    def accao(self):
        return self.__accao

    def aplicar(self, estado: Estado) -> Estado:
        from agente_prosp.controlo_delib.modelo.estado_agente import EstadoAgente
        nova_posicao = self._translacao(estado.posicao, 1, self.ang)
        novo_estado = EstadoAgente(nova_posicao)
        if novo_estado in self.__modelo_mundo:
            return novo_estado
        return None

    def _translacao(self, posicao, distancia, angulo):
        x = posicao[0] + round(distancia * math.cos(angulo))
        y = posicao[1] + round(distancia * math.sin(angulo))
        return (x, y)

    def custo(self, estado: Estado, estado_suc: Estado) -> float:
        dx = abs(estado.posicao[0] - estado_suc.posicao[0])
        dy = abs(estado.posicao[1] - estado_suc.posicao[1])
        return max(dx, dy)

    def __repr__(self):
        return "OperadorMover(%s)" % self.accao