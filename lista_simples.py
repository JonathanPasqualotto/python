import os

class listas_simples:
    def __init__(self):
        self.FimLista = -1
        self.Lista = [0]*10
    
    def Lista_Vazia(self):
        return self.FimLista == -1

    def ValidaInsercao(self):
        return (self.FimLista + 1) != 10

    def InsereFimLista(self,valor):
        if self.ValidaInsercao():
            self.FimLista = self.FimLista +1
            self.Lista[self.FimLista] = valor
        
    def MostrarLista(self):
        if not self.Lista_Vazia():
            for i in range(0,self.FimLista + 1):
                print('%d '%self.Lista[i],end=' ')
    
    def InsereKelemento(self,valor,indice):
        self.Lista[indice+1] = valor


 #   def RemoveKElemento(self,indice):
 #       self.Lista[indice] = 


lista = listas_simples()
while True:
    os.system('clear')
    print('''
    1 - Inserir valor no fim da lista.
    2 - Inserir valor no k-ésimo elemento da lista
    3 - Remover valor no k-ésimo elemento da lista
    4 - Pesquisar valor no k-ésimo eçemento da lista
    5 - Pesquisa valor na lista.
    6 - Mostrar lista.
    0 - Sair''')
    op = int(input('Entre com a opçã desejada: '))
    if op == 0:
        break
    elif op == 1:
        if lista.ValidaInsercao():
            valor = int(input('Entre com o valor a ser inserido: '))
            lista.InsereFimLista(valor)
        else:
            print('Lista cheia!')
    elif op == 6:
        lista.MostrarLista()
    elif op == 2:
        if not lista.Lista_Vazia():
            indice = int(input('Entre com o valor do Indice: '))
            valor = int(input('Entre com o valor a ser inserido: '))
            lista.InsereKelemento(valor, indice)
    elif op == 3:
        if not lista.Lista_Vazia():
            indice = int(input('Entre com o valor do Indice: '))
            lista.RemoveKElemento(indice)


    input('\nDigite uma tecla para continuar.')