class NodoArvore:
    def __init(self, chave=None,esquerda=None,direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return '%s' %(self.chave)

class ArvoreBinaria:
    def __init__(self):
        self.inicio = None

    def ArvoreVazia(self,raiz):
        return raiz == None

