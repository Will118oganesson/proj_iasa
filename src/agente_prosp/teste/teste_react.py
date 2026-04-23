from sae import Simulador

from agente_prosp.agente_prosp import AgenteProsp
from agente_prosp.controlo_react.controlo_react import ControloReact
from agente_prosp.controlo_react.reaccoes.recolher.recolher import Recolher


if __name__ == "__main__":
    comportamento = Recolher()
    controlo = ControloReact(comportamento)
    agente = AgenteProsp(controlo)
    simulador = Simulador(1,agente, vista_modelo = True)
    simulador.executar()