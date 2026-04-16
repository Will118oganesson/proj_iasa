#estimulo ao alvo detectado, com base na direçao de percepçao e gama(fator de decaimento da 
    #intensidade do estimulo)
from sae import Elemento
from lib.ecr.estimulo import Estimulo

class EstimuloAlvo(Estimulo):
    def __init__(self, direccao, gama=0.9):
        self.__direccao = direccao
        self.__gama = gama

    def detectar(self, percepcao):
        elemento, distancia, _ = percepcao[self.__direccao]
        if elemento == Elemento.ALVO:
            return self.__gama ** distancia
        return 0