from sae import Simulador

from agente_prosp.agente_prosp import AgenteProsp
from agente_prosp.controlo_delib.controlo_delib import ControloDelib
from plan.plan_pee.planeador_pee import PlaneadorPEE


if __name__ == "__main__":
    planeador = PlaneadorPEE()
    controlo = ControloDelib(planeador)
    agente = AgenteProsp(controlo)
    simulador = Simulador(3, agente, vista_modelo=True)
    simulador.executar()