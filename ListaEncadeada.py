import os

class No:
    def __init__(self,info):
        self.info = info
        self.proximo = None
    
    def RetornaInfo(self):
        return self.info
    
    def RetornaProximo(self):
        return self.proximo
    
    def InsereInfo(self,NovaInfo):
        self.info = NovaInfo
        
    def InsereProximo(self,NovoProximo):
        self.proximo = NovoProximo
        

class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def ListaVazia(self):
        return self.inicio == None

    def Inserir(self,item):
        Novoitem =  No(item)         
        Novoitem.InsereProximo(self.inicio)
        self.inicio = Novoitem
    
    def Imprimir(self):
        atual = self.inicio
        while atual != None:
            print(atual.RetornaInfo())
            atual = atual.RetornaProximo()       
    
    def Buscar(self,item):
        atual = self.inicio
        encontrou = False
        while atual != None and not encontrou:
            if atual.RetornaInfo() == item:
                encontrou = True
            else:
                atual = atual.RetornaProximo()
        return encontrou
        
    def Remover(self,item):
        ant = None
        atual = self.inicio
        encontrou = False
        while atual != None and not encontrou:            
            if atual.RetornaInfo() == item:
                if ant == None:
                    self.inicio = atual.RetornaProximo()
                else:
                    ant.InsereProximo(atual.RetornaProximo())
                encontrou = True
                break
            ant = atual
            atual = atual.RetornaProximo()            
        return encontrou

Lista = ListaEncadeada()
while True:
    os.system('clear')
    print("1 - Insere valores na lista.")
    print("2 - Exibir Lista.")
    print("3 - Buscar valor.")
    print("4 - Remover valor.")
    print("0 - Sair.")
    OP = int(input("Entre com a opção desejada: "))
    if OP == 0:
        break
    elif OP == 1:
        valor = int(input("Entre com o valor: "))
        Lista.Inserir(valor)
    elif OP == 2:
        Lista.Imprimir()
    elif OP == 3:
        valor = int(input("Entre com o valor a ser encontrado: "))
        if Lista.Buscar(valor):
            print("Valor %d encontrado na lista."%valor)
        else:
            print("Valor %d não foi encontrado na lista."%valor)
    elif OP == 4:            
        valor = int(input("Entre com o valor a ser removido: "))
        if Lista.Remover(valor):
            print("Valor %d removido com sucesso."%valor)
            Lista.Imprimir()
        else:
            print("Valor %d não foi encontrado para remoção da lista."%valor)
    else:    
      print("OPCAO INVALIDA!!!!!!!!!!!")                       
    input("Digite uma tecla para continuar.")  