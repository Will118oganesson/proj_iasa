from lib.agente.Controlo import Controlo

TRANSICOES = []

class ControloPersonagem(Controlo):
    
    def __init__(self, percepcao):
        self.percepcao = percepcao
    
    def processar(self, precepcao):
        return "Accao"