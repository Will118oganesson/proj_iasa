import math
from sae import Direccao, Elemento

from .estado_agente import EstadoAgente
from lib.plan.modelo.modelo_plan import ModeloPlan
from .operador_mover import OperadorMover

class ModeloMundo(ModeloPlan):

    def __init__(self):
        self.__estado = None
        self.__estados = []
        self.__elementos = {}
        self.__operadores = [OperadorMover(self, direccao) for direccao in Direccao]
        self.__alterado = False
    
    @property
    def alterado(self):
        return self.__alterado
    
    @property
    def elementos(self):
        return self.__elementos
    
    def __contains__(self, estado):
        return estado in self.__estados

    def obter_estado(self):
        return self.__estado
    
    def obter_estados(self):
        return self.__estados
    
    def obter_operadores(self):
        return self.__operadores

    def obter_elemento(self, estado):
        return self.__elemento.get(estado.posicao)
   
    def distancia(self, estado):
        return math.dist(estado.posicao, self.__estado.posicao)
    
    def actualizar(self, percepcao):
        self.__estado = EstadoAgente(percepcao.posicao)
        self.__alterado = self.__elementos != percepcao.elementos
        if self.__alterado:
            self.__elementos = percepcao.elementos
            self.__estados = [EstadoAgente(posicao) for posicao in percepcao.posicoes]

    def mostrar(self, vista):
        for posicao, elemento in self .__elementos.items():
            if elemento in [Elemento.ALVO , Elemento.OBSTACULO]:
                vista.mostrar_elemento(posicao, elemento)
        vista.marcar_posicao(self.__estado.posicao)