from enum import Enum

class EventoJogo(Enum):
    SILENCIO = 'silencio'
    RUIDO = 'ruido'
    ANIMAL = 'animal'
    FUGA = 'fuga'
    FOTOGRAFIA = 'fotografia'
    TERMINAR = 'terminar'

    def mostrar(self):
        print(self)