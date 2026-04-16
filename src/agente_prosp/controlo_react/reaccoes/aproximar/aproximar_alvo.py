from sae import Direccao
from lib.ecr.prioridade import Prioridade
from .aproximar_dir import AproximarDir

class AproximarAlvo(Prioridade):
     def __init__(self):
        super().__init__([
            # AproximarDir(Direccao.NORTE),
            # AproximarDir(Direccao.SUL),
            # AproximarDir(Direccao.ESTE),
            # AproximarDir(Direccao.OESTE),
            AproximarDir(direccao) for direccao in Direccao
        ])