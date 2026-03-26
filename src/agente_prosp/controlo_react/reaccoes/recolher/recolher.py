from lib.ecr.hierarquia import Hierarquia
# from agente_prosp.controlo_react.reaccoes.aproximar.aproximar_alvo import AproximarAlvo
# from agente_prosp.controlo_react.reaccoes.evitar.evitar_obs import EvitarObst
# from agente_prosp.controlo_react.reaccoes.explorar.explorar import Explorar


class Recolher(Hierarquia):
    def __init__(self):
        super().__init__([
            #AproximarAlvo(),
            #EvitarObst(),
            #explorar_mem()
            #Explorar()
        ])