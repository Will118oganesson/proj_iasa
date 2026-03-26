from sae import Simulador

from agente_prosp.agente_prosp import AgenteProsp
from agente_prosp.controlo_react.controlo_react import ControloReact
from agente_prosp.controlo_react.reaccoes.recolher.recolher import Recolher

import recolher_Stub

if __name__ == "__main__":
    comportamento = recolher_Stub.RecolherStub()
    controlo = ControloReact(comportamento)
    agente = AgenteProsp(controlo)
    simulador = Simulador(2,agente)
    simulador.executar()