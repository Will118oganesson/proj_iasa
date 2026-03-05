from ambiente.AmbienteJogo import AmbienteJogo
from agente.Agente import Agente

class AgenteJogo(Agente):
    def __init__(self, ambiente: AmbienteJogo, controlo):
        super().__init__(controlo)
        self.__ambiente = ambiente

    def _percepcionar(self):
        return self.__ambiente.observar()
    
    def _actuar(self, accao):
        self.__ambiente.executar(accao)
    