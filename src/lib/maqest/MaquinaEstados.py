class MaquinaEstados:
    def __init__(self, estado_inicial, transicoes):
        self.__estado = estado_inicial

        self.__tte = {}
        self.__tae = {}

        if transicoes:
            for transicao in transicoes:
                estado_ant, evento, estado_suc, accao = transicao if len(transicao) == 4 else transicao + (None,)
                self.definir_transicao(estado_ant, evento, estado_suc, accao)

    def definir_transicao(self, estado_ant, evento, estado_suc, accao=None):
        self.__tte[(estado_ant, evento)] = estado_suc
        if accao is not None:
            self.__tae[(estado_ant, evento)] = accao

    def processar(self, evento):

        novo_estado = self.__tte.get((self.__estado, evento))
        if novo_estado is not None:
            self.__estado = novo_estado

        accao = self.__tae.get((self.__estado, evento))
        return accao

