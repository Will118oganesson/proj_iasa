
from .ControloPersonagem import ControloPersonagem
from ambiente.AmbienteJogo import AmbienteJogo
from agente.AgenteJogo import AgenteJogo

class Personagem(AgenteJogo):
    
    def __init__(self, ambiente : AmbienteJogo):
        super().__init__(ambiente, ControloPersonagem())
        #self.__ambiente = ambiente
        
        
    
    def mostrar(self):
        print(self)