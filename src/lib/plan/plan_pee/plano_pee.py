from sae.vistas.vista_amb import VistaAmb
from pee.mec_proc.solucao import Solucao
from mod.operador import Operador
from mod.estado import Estado

class PlanoPEE:
    def __init__(self, solucao: Solucao, estado_inicial: Estado):
        passos = solucao.obter_passos() if hasattr(solucao, 'obter_passos') else []

        self._operadores = []      # para consumir durante a execução
        self._vectores = []        # para mostrar as setas (posição, ângulo)

        estado_atual = estado_inicial
        for passo in passos:
            self._operadores.append(passo.operador)
            # Guarda a posição de onde parte a seta e o ângulo do operador
            self._vectores.append((estado_atual.posicao, passo.operador.angulo))
            estado_atual = passo.estado   # avança para o estado seguinte

    def obter_accao(self, estado) -> Operador:
        """Devolve o próximo operador do plano, ou None se o plano estiver vazio."""
        if not self._operadores:
            return None
        # Não compara estados – confia no plano
        return self._operadores.pop(0)

    def mostrar(self, vista: VistaAmb):
        """Desenha setas na vista para ilustrar o plano."""
        for posicao, angulo in self._vectores:
            vista.mostrar_vector(posicao, -angulo)