import os

class ClasseListaLinear:
    def __init__(self):
        self.FimLista = -1
        self.Lista = [0]*10
        
    def ListaVazia(self):
        return self.FimLista == -1
    
    def ValidaInsercao(self):
        return (self.FimLista + 1) != 10
    
    def InsereFimLista(self,Valor):
        if self.ValidaInsercao():
            self.FimLista = self.FimLista + 1
            self.Lista[self.FimLista] = Valor
            
    def Insere_k_esimo_Elemento(self,Valor,k):
        if k > self.FimLista or k < 0:
            print("K-ésimo elemento não existe.")
        else:
            i = self.FimLista
            while i >= k:
                self.Lista[i+1] = self.Lista[i]
                i -= 1
            self.Lista[k] = Valor
            self.FimLista += 1
                
    def MostrarLista(self):
        if not self.ListaVazia():
            for i in range(0,self.FimLista + 1):
                print("%d "%self.Lista[i],end="")


ListaLinear = ClasseListaLinear()
while True:
    os.system('cls')
    print("1 - Inserir valor no fim da lista.")
    print("2 - Inserir valor no K-esimo elemento da lista.")
    print("3 - Remover valor no K-esimo elemento da lista.")
    print("4 - Pesquisar valor no K-esimo elemento da lista.")
    print("5 - Pesquisa valor na lista.")
    print("6 - Mostrar lista.")
    print("0 - Sair.")
    OP = int(input("Entre com a opção desejada: "))
    if OP == 0:
        break
    elif OP == 1:
        if ListaLinear.ValidaInsercao():
            Valor = int(input("Entre com o valor a ser inserido: "))
            ListaLinear.InsereFimLista(Valor)
        else:
            print("Lista Cheia")
    elif OP == 2:            
        if ListaLinear.ValidaInsercao():
            Valor,Indice = map(int,input("Entre com o valor e o local (índice) a ser inserido: ").split())
            ListaLinear.Insere_k_esimo_Elemento(Valor,Indice)
        else:
            print("Lista Cheia")
        
    elif OP == 6:
        ListaLinear.MostrarLista()
        

    input("Digite uma tecla para continuar.")  