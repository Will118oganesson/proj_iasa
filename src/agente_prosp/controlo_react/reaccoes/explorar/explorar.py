from lib.ecr.comportamento import Comportamento
import random
from agente_prosp.accoes.avancar import Avancar
from agente_prosp.accoes.rodar import Rodar

#explorar é um comportamente que explora com direçoes aleatorios

class Explorar(Comportamento):
    def __init__(self, prob_rotacao=0.7):
        self.__prob_rotacao = prob_rotacao
        self.__avancar = Avancar()

    def activar(self, percepcao):
        if percepcao.contacto_obst() or random.random() < self.__prob_rotacao:
            novaDir = percepcao.direccao.rodar(random.choice([1,-1]))
            return Rodar(novaDir)
        return self.__avancar