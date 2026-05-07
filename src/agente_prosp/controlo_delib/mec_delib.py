from agente_prosp.controlo_delib.modelo.modelo_mundo import ModeloMundo
from agente_prosp.controlo_delib.modelo.estado_agente import EstadoAgente
from sae import Elemento

class MecDelib:
    def __init__(self, modelo_mundo: ModeloMundo):
        pass
    def deliberar(self) -> list[EstadoAgente]:
        pass
    def _gerar_objetivos(self) -> list[EstadoAgente]:
        # States whose position holds an ALVO element become goals
        return [
            estado
            for estado in self.__modelo_mundo.obter_estados()
            if self.__modelo_mundo.obter_elemento(estado) == Elemento.ALVO
        ]
    def _seleccionar_objetivos(self, objectivos: list[EstadoAgente]) -> list[EstadoAgente]:
        # Sort nearest-first using the model's distance from the agent
        return sorted(objectivos, key=lambda obj: self.__modelo_mundo.distancia(obj))