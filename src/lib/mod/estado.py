class Estado:
    def __init__(self, posicao):
        self.posicao = posicao   # tuple (x, y)

    def id_valor(self) -> int:
        """Devolve um identificador único para este estado (usado em conjuntos)."""
        return hash(self.posicao)

    def __eq__(self, other):
        return isinstance(other, Estado) and self.posicao == other.posicao

    def __hash__(self):
        return hash(self.posicao)