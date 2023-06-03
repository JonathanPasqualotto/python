class Nodo:
    def __init__(self, chave=None, esq=None, dir=None):
        self.chave = chave
        self.esq = esq
        self.dir = dir

    def __repr__(self):
        return '%s' % (self.chave)

class Arvore:
    def __init__(self):
        self.inicio = None
        
    def ArvoreVazia(self,raiz):
        return raiz == None
        
    def insere(self, raiz, nodo):
        if raiz is None:
            raiz = nodo
        elif (nodo.chave) > (raiz.chave):
            if raiz.dir is None:
                raiz.dir = nodo
            else:
                self.insere(raiz.dir, nodo)
        else:
            if raiz.esq is None:
                raiz.esq = nodo
            else:
                self.insere(raiz.esq, nodo)

    def pre_ordem(self, raiz, listar):
        if not raiz:
            return listar
        listar.append(raiz.__repr__())
        self.pre_ordem(raiz.esq, listar)
        self.pre_ordem(raiz.dir, listar)
        
    def in_ordem(self, raiz, listar):
        if not raiz:
            return listar
        self.in_ordem(raiz.esq, listar)
        listar.append(raiz.__repr__())
        self.in_ordem(raiz.dir, listar)
        
    def pos_ordem(self, raiz, listar):
        if not raiz:
            return listar
        self.pos_ordem(raiz.esq, listar)
        self.pos_ordem(raiz.dir, listar)
        listar.append(raiz.__repr__())
        
    def find(self, raiz, n, listar):
        self.in_ordem(raiz, listar)
        if n in listar:
            print('%s existe'%n)
        else:
            print('%s nao existe'%n)
    
          
while True:
    try:
        Arvore = Arvore()
        raiz = None
        while True:
            entrada = input()
            lista = entrada.split()
            if lista[0] == 'I':
                if Arvore.ArvoreVazia(raiz):            
                    raiz = Nodo(lista[1])
                else:
                    nodo = Nodo(lista[1])
                    Arvore.insere(raiz,nodo)     
            elif lista[0] == 'INFIXA':
                listar = []
                Arvore.in_ordem(raiz, listar)
                print(*listar)
        
            elif lista[0] == 'PREFIXA':
                listar = []
                Arvore.pre_ordem(raiz, listar)
                print(*listar)
        
            elif lista[0] == 'POSFIXA':
                listar = []        
                Arvore.pos_ordem(raiz, listar)
                print(*listar)
        
            elif lista[0] == 'P':
                listar = []
                Arvore.find(raiz, lista[1], listar)
    except EOFError:
        break