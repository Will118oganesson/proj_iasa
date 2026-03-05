from ambiente.AmbienteJogo import AmbienteJogo
from personagem.Personagem import Personagem

class Jogo:
    def __init__(self):
        self.__ambiente = AmbienteJogo()
        self.__personagem = Personagem(self.__ambiente)
        self.__personagem.mostrar()

    def executar(self):
         while self.__ambiente.evoluir():
            self.__personagem.executar()
            self.__personagem.mostrar()


if __name__ == "__main__":
    jogo = Jogo()
    jogo.executar()