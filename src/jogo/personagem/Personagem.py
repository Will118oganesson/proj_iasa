from agente.AgenteJogo import AgenteJogo

class Personagem(AgenteJogo):
    
    def __init__(self, ambiente):
        self.ambiente = ambiente
    
    def mostrar(self):
        print(self)