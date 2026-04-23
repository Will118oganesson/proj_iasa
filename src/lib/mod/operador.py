from estado import Estado

class Operador:
    def aplicar(self, estado: Estado) -> Estado:
        raise NotImplementedError
    def custo(self, estado: Estado, estado_suc: Estado) -> float:
        raise NotImplementedError