from enum import Enum

class EstadoPersonagem(Enum):
    PROCURA = 0
    INSPECCAO = 1
    OBSERVACAO = 2
    REGISTO = 3

    def mostrar(self):
        print(f"Estado: {self.name}")