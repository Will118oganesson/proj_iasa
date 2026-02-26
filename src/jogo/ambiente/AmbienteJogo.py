from .EventoJogo import EventoJogo
from .ComandoJogo import ComandoJogo

class AmbienteJogo:
    def __init__(self):
        self.events = [event.value for event in EventoJogo]
        pass
    def observar(self):
        pass
    def executar(comando):
        if comando not in ComandoJogo:
            pass
        pass
    def __gerar_evento(self):
        return
