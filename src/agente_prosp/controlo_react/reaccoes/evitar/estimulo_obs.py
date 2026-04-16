from lib.ecr.estimulo import Estimulo
from lib.sae import Elemento
    
#estimulo ao obstaculo, com base na direçao de percepçao e gama(fator de decaimento da intensidade do estimulo)

class EstimuloObst(Estimulo):
    INTENS_OBST = 1

    def detectar(self, percepcao):
        elemento, distancia, _ = percepcao[percepcao.direccao]
        if (elemento == Elemento.OBSTACULO and distancia == 1) or (elemento is None and distancia == 0):
            return self.INTENS_OBST
        return 0