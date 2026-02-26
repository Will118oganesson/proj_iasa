from enum import Enum

class EventoJogo(Enum):
    SILENCIO = 's'
    RUIDO = 'r'
    ANIMAL = 'a'
    FUGA = 'f'
    FOTOGRAFIA = 'p'
    TERMINAR = 't'

    def mostrar(self):
        print(self)