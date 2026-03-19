from sae.agente.movimento import Movimento

class Recolher:
    def executar(self, percepcao):
        if percepcao.contacto_obst():
            nova_dir = percepcao.direccao.rodar(1)
            return Movimento(nova_dir, passo=0)
        return Movimento(percepcao.direccao)