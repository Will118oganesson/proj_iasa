import sae
from lib.agente.Agente import Agente

class AgenteProsp(Agente):
        
    def _percepcionar(self):
        return sae.transdutor.percepcionar()
        

    def _actuar(self, accao):
        sae.transdutor.actuar(accao.movimento)
