from lib.ecr.comportamento import Comportamento

from agente_prosp.accoes.avancar import Avancar
from agente_prosp.accoes.rodar import Rodar

class ExplorarMem(Comportamento):
    def __init__(self, dim_max_mem = 100):
        self.__dim_max_mem = dim_max_mem
        self.__accao = Avancar()
        self.__memoria = [] # tuplos com posiçao e direccao

    def activar(self, percepcao): #requires modification
        situacao = (percepcao.posicao, percepcao.direccao)
        if (situacao not in self.__memoria):
            self.__memoria.append(situacao)
            if(len(self.__memoria) > self.__dim_max_mem):
                self.__memoria.pop(0)

            return self.__accao
        ## logica de explorar mais um save na memoria
