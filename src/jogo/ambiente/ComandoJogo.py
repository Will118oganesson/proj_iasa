from enum import Enum

class ComandoJogo(Enum):

    PROCURAR = 0
    APROXIMAR = 1
    OBSERVAR = 2
    FOTOGRAFAR = 3

    def mostrar(self):
        print(self)