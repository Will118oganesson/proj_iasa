
from .ControloPersonagem import ControloPersonagem
from ambiente.AmbienteJogo import AmbienteJogo
from agente.AgenteJogo import AgenteJogo

class Personagem(AgenteJogo):
    
    def __init__(self, ambiente : AmbienteJogo):
        super().__init__(ambiente, ControloPersonagem())
        #self.__ambiente = ambiente
        
        
    
    def mostrar(self):
        print(self)

    def __str__(self):

        controlo = self._controlo()

        estado = controlo.estado()
        accao = controlo.accao()

        if accao is not None:
            comando = accao.comando()
            return f"{estado.name} -> {comando.name}"

        return f"{estado.name}"