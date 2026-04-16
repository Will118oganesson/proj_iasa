class Resposta:
    def __init__(self, accao=None):
        self._accao = accao
        
    def activar(self, percepcao, intensidade=0):
        accao = self._obter_accao(percepcao)
        if accao:
            accao.prioridade = intensidade
        return accao 
    
    def _obter_accao(self, percepcao):
        return self._accao