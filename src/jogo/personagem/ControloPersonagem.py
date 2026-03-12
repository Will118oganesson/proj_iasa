from lib.agente.Controlo import Controlo
from maqest.MaquinaEstados import MaquinaEstados
from .EstadoPersonagem import EstadoPersonagem
from agente.AccaoJogo import AccaoJogo
from ambiente.ComandoJogo import ComandoJogo
from ambiente.EventoJogo import EventoJogo


class ControloPersonagem(Controlo):
    
    def __init__(self):
        self.__accao = None

        procurar = AccaoJogo(ComandoJogo.PROCURAR)
        aproximar = AccaoJogo(ComandoJogo.APROXIMAR)
        observar = AccaoJogo(ComandoJogo.OBSERVAR)
        fotografar = AccaoJogo(ComandoJogo.FOTOGRAFAR)

        self.__maq_est = MaquinaEstados(
            EstadoPersonagem.PROCURA, [
                (EstadoPersonagem.PROCURA, EventoJogo.ANIMAL,EstadoPersonagem.OBSERVACAO,aproximar),
                (EstadoPersonagem.PROCURA, EventoJogo.RUIDO,EstadoPersonagem.INSPECCAO,aproximar),
                (EstadoPersonagem.PROCURA, EventoJogo.SILENCIO,EstadoPersonagem.PROCURA,procurar),
                (EstadoPersonagem.INSPECCAO, EventoJogo.ANIMAL,EstadoPersonagem.OBSERVACAO,aproximar),
                (EstadoPersonagem.INSPECCAO, EventoJogo.RUIDO,EstadoPersonagem.INSPECCAO,procurar),
                (EstadoPersonagem.INSPECCAO, EventoJogo.SILENCIO,EstadoPersonagem.PROCURA),
                (EstadoPersonagem.OBSERVACAO, EventoJogo.FUGA,EstadoPersonagem.INSPECCAO),
                (EstadoPersonagem.OBSERVACAO, EventoJogo.ANIMAL,EstadoPersonagem.REGISTO, observar),
                (EstadoPersonagem.REGISTO, EventoJogo.ANIMAL,EstadoPersonagem.REGISTO, fotografar),
                (EstadoPersonagem.REGISTO, EventoJogo.FUGA,EstadoPersonagem.PROCURA),
                (EstadoPersonagem.REGISTO, EventoJogo.FOTOGRAFIA,EstadoPersonagem.PROCURA),
            ]
        )

    def estado(self):
        return self.__maq_est.estado()
    
    def processar(self, percepcao):
        evento = percepcao.evento()
        self.__accao = self.__maq_est.processar(evento)
        return self.__accao
    
    def accao(self):
        return self.__accao