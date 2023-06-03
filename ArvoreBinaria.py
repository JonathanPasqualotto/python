#Referencia - https://algoritmosempython.com.br/cursos/algoritmos-python/estruturas-dados/arvores/

import os

class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave,
                                    self.chave,
                                    self.direita and self.direita.chave)

class ArvoreBinaria:
    def __init__(self):
        self.inicio = None
        
    def ArvoreVazia(self,raiz):
        return raiz == None
        
    def insere(self, raiz, nodo):
        """Insere um nodo em uma �rvore bin�ria de pesquisa."""
        # Nodo deve ser inserido na raiz.
        if raiz is None:
            print('Nodo Raiz')
            raiz = nodo
        # Nodo deve ser inserido na sub�rvore direita.
        elif int(nodo.chave) > int(raiz.chave):
            print(raiz.chave," -> ",nodo.chave)
            print('Inseriu a direita')
            if raiz.direita is None:
                raiz.direita = nodo
            else:
                self.insere(raiz.direita, nodo)
        # Nodo deve ser inserido na sub�rvore esquerda.
        else:
            print(nodo.chave," <- ",raiz.chave)
            print('Inseriu a esquerda')
            if raiz.esquerda is None:
                raiz.esquerda = nodo
            else:
                self.insere(raiz.esquerda, nodo)

    def pre_ordem(self, raiz):
        if not raiz:
            return
        # Visita nodo corrente.
        #print(raiz)
        print(raiz.__repr__())
        # Visita filho da esquerda.
        self.pre_ordem(raiz.esquerda)
        # Visita filho da direita.
        self.pre_ordem(raiz.direita)
        
    def in_ordem(self, raiz):
        if not raiz:
            return
        
        self.in_ordem(raiz.esquerda)
        print(raiz.__repr__())
        self.in_ordem(raiz.direita)
        
    def pos_ordem(self, raiz):
        if not raiz:
            return
        self.in_ordem(raiz.esquerda)
        self.in_ordem(raiz.direita)
        print(raiz.__repr__())
          
Arvore = ArvoreBinaria()
raiz = None
while True:
    os.system('clear')
    print("1 - Insere valores na árvore.")
    print("2 - Exibir Pré-ordem.")
    print("3 - Exibir In-ordem.")    
    print("4 - Exibir Pós-ordem.")
    print("0 - Sair.")
    OP = int(input("Entre com a operação desejada: "))
    if OP == 0:
        break
    elif OP == 1:
        valor = input("Entre com o valor: ")
        if Arvore.ArvoreVazia(raiz):            
            raiz = NodoArvore(valor)
        else:
            nodo = NodoArvore(valor)
            Arvore.insere(raiz,nodo)        
    elif OP == 2:
        if Arvore.ArvoreVazia(raiz):
            print("ÁRVORE VAZIA!!!!!!!!!!!")                       
        Arvore.pre_ordem(raiz)        
    elif OP == 3:
        if Arvore.ArvoreVazia(raiz):
            print("ÁRVORE VAZIA!!!!!!!!!!!")                       
        Arvore.in_ordem(raiz)                      
    elif OP == 4:
        if Arvore.ArvoreVazia(raiz):
            print("ÁRVORE VAZIA!!!!!!!!!!!")                       
        Arvore.pos_ordem(raiz)                      
    else:
      print("OPçÃO INVALIDA!!!!!!!!!!!")                       
    input("Digite uma tecla para continuar.")  