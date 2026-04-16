from ecr.accao import Accao
from ecr.comportamento import Comportamento
#
class Reaccao(Comportamento):
    def __init__(self, estimulo, resposta):
        self.__estimulo = estimulo
        self.__resposta = resposta

    def activar(self, percepcao) -> Accao:
        # Perguntar ao estímulo se está a detetar algo
        # O detectar devolve 0.0 se não detetou nada
        # O detectar devolve um valor maior que 0 se detetou algo
        # Comentarios de explicaçao dados por um colega
        intensidade = self.__estimulo.detectar(percepcao)

        if intensidade > 0:
            # O estímulo detetou algo, então ativar a resposta
            # A intensidade vai definir a prioridade da ação
            return self.__resposta.activar(percepcao, intensidade)
        
        return None