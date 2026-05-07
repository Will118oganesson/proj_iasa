from plan.plan_pee.planeador_pee import PlaneadorPEE
from lib.agente.Controlo import Controlo
from agente.Percepcao import Percepcao
from agente.Accao import Accao
from agente_prosp.controlo_delib.modelo.modelo_mundo import ModeloMundo
from .mec_delib import MecDelib
from lib import sae


class ControloDelib(Controlo): #responsavel pelo controlo deliberativo do agente
    def _init_(self, planeador: PlaneadorPEE):
        self.__modelo_mundo = ModeloMundo()
        self.__mec_delib = MecDelib(ModeloMundo())
        self.__planeador = planeador
        self.__objectivos = None
        self.__plano = None
    #INIT DONE

    def processar(self, percepcao: Percepcao): #obj: processar a percepcao
        #self assimilar percepcao
        self.__assimilar(percepcao)
        if (self.__reconsiderar()): #existe reconsiderar?:
            self.__deliberar()
            self.__planear()
        return self.__executar()
        #return super().processar(percepcao)
    #PROCESSAR DONE SUPPOSEDLY
    
    def __assimilar(self, percepcao: Percepcao): #obj: atualizr as crenças de acordo com a percepcao
        self.__modelo_mundo.actualizar(percepcao)
    #ASSIMILAR DONE

    def __reconsiderar(self) -> bool: #retorna modelomundo alterado | retorno modelomundo alterado ou nao o plano
        self.__modelo_mundo.alterado or not self._plano

    def __deliberar(self): #obj: 
        self.objectivos = self.__mec_delib.deliberar()
        #no return

    def __planear(self): #obj: gerar plano de accao para objetivos
        if (self.objectivos): #entao carrego objetivos no plano
            self._plano = self._planeador.planear(self._modelomundo, self._objetivos)
        else: #entao n ha plano
            self._plano = None

    def __executar(self) -> Accao: #gerar uma acao a executar para atingir os objetivos
        self.__mostrar()
        if (self._plano):
            estado = self._modelomundo.obter_estado()
            operador = self._plano.obter_accao(estado) # recebo operador
            #operador recebe modelomundo.obteroperador
            if (operador):
                return operador.accao
            else:
                return None
        return Accao


    def __mostrar(self): #obj: mostrat info interna
        sae.vista.limpar()
        self.__modelo_mundo.mostrar(sae.vista)
        if (self._plano):
            self._plano.mostrar(sae.vista)
        if (self._objetivos):
            for objetivo in self._objetivos:
                sae.vista.marcar_posicao(objetivo.posicao)