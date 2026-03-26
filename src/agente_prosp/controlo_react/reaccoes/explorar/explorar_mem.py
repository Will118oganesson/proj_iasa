from lib.ecr.comportamento import Comportamento

class ExplorarMem(Comportamento):
    dim_max_mem
    memoria = [] # tuplos com posiçao e direccao

    def __init__(self, dim_max_mem = 100):
        pass

    def activar(self, percepcao): #requires modification
        return super().activar(percepcao)
        ## logica de explorar mais um save na memoria
