from mec_proc.fronteira import Fronteira
from aval.avaliador import Avaliador
from mec_proc.no import No

class FronteiraPrioridade(Fronteira):
    def __init__(self, avaliador: Avaliador):
        self.avaliador = avaliador

    def inserir(self, no: No):
        raise NotImplementedError
    
    def remover(self) -> No:
        raise NotImplementedError