from .EventoJogo import EventoJogo
from .ComandoJogo import ComandoJogo
from agente.PercepcaoJogo import PercecaoJogo

class AmbienteJogo:
    def __init__(self):
        self.events = [event.value for event in EventoJogo]
        self.__event = EventoJogo.SILENCIO

    def observar(self):
        return PercecaoJogo(self.__event)
    
    def evoluir(self) -> bool:
        self.__event = self.__gerar_evento()
        if self.__event is not None:
            self.__event.mostrar()
        return self.__event != EventoJogo.TERMINAR

    def executar(self, comando):
        comando.mostrar()

    # def __gerar_evento(self):
    #     self.__event = input("Evento?:")
    #     if self.__event == "help":
    #         print(self.events)
    #         return
    #     if self.__event not in self.events:
    #         self.__event = EventoJogo.SILENCIO
    def __gerar_evento(self):

        evento = input("Evento?: ")

        if evento == "help":
            print(self.events)
            return EventoJogo.SILENCIO

        if evento not in self.events:
            return EventoJogo.SILENCIO

        return EventoJogo(evento)

            


