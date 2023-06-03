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
        if raiz is None:
            print('Nodo Raiz')
            raiz = nodo
        elif int(nodo.chave) > int(raiz.chave):
            print(raiz.chave," -> ",nodo.chave)
            print('Inseriu a direita')
            if raiz.direita is None:
                raiz.direita = nodo
            else:
                self.insere(raiz.direita, nodo)
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
        print(raiz.__repr__())
        self.pre_ordem(raiz.esquerda)
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
        self.pos_ordem(raiz.esquerda)
        self.pos_ordem(raiz.direita)
        print(raiz.__repr__())
    
    def ContaNodos(self, raiz):
        if raiz == None:
            return 0
        soma = 1 + self.ContaNodos(raiz.esquerda) + self.ContaNodos(raiz.direita)
        print(raiz.__repr__())
        return soma


          

Arvore = ArvoreBinaria()
raiz = None
par = 0
impar = 0
while True:
    os.system('clear')
    print('''
    1 - Inserir nodos na árvore
    2 - Exibir PRÉ-ORDEM.
    3 - Exibir INFIXADO    
    4 - Exibir PÓS-ORDEM
    5 - Mostrar e contar quantos nodos internos tem a árvore
    6 - Contar quantos nós são pares
    7 - Somar os nós ímpares
    0 - Sair.''')
    opacao = int(input("Entre com a operação desejada: "))
    if opacao == 0:
        exit()
    elif opacao == 1:
        valor = input("Entre com o valor: ")
        if int(valor) % 2 == 0:
            if Arvore.ArvoreVazia(raiz):
                raiz = NodoArvore(valor)
                par += 1
            else:
                nodo = NodoArvore(valor)
                Arvore.insere(raiz,nodo)
                par += 1
        else:
            if Arvore.ArvoreVazia(raiz):
                raiz = NodoArvore(valor)
                impar += int(valor)
            else:
                nodo = NodoArvore(valor)
                Arvore.insere(raiz,nodo)
                impar += int(valor)
    elif opacao == 2:
        if Arvore.ArvoreVazia(raiz):
            print("Árvore Vazia!")                       
        Arvore.pre_ordem(raiz)        
    elif opacao == 3:
        if Arvore.ArvoreVazia(raiz):
            print("Árvore Vazia!")                       
        Arvore.in_ordem(raiz)                      
    elif opacao == 4:
        if Arvore.ArvoreVazia(raiz):
            print("Árvore Vazia!")                       
        Arvore.pos_ordem(raiz)              
    elif opacao == 5:
        if Arvore.ArvoreVazia(raiz):
            print("Árvore Vazia!") 
        print(Arvore.ContaNodos(raiz))
    elif opacao == 6:
        if Arvore.ArvoreVazia(raiz):
            print("Árvore Vazia!")
        print(par)
    elif opacao == 7:
        if Arvore.ArvoreVazia(raiz):
            print("Árvore Vazia!")
        print(impar)
    else:
      print("Opção INVÁLIDA! favor verificar")                       
    input("Digite uma tecla para continuar.")  