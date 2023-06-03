import os


class ClassePilha:    
    def __init__(self):
        self.TOPO = -1
        self.Pilha = [0]*10
        
    def PilhaVazia(self):
        return self.TOPO == -1
    
    def PilhaCheia(self):
        return self.TOPO == 10-1
       
    def PUSH(self,Valor):
        self.TOPO = self.TOPO + 1
        self.Pilha[self.TOPO] = Valor
        
    def POP(self):
        Valor = self.Pilha[self.TOPO]
        self.TOPO = self.TOPO - 1
        return Valor
        
    def ExibirLista(self):
        PilhaCopia = self.Pilha
        while self.TOPO != -1:
            print(self.POP())
        Pilha = PilhaCopia
        

Pilha = ClassePilha()
while True:
    os.system('clear')
    print("1 - Empilha.")
    print("2 - Desempilha.")
    print("3 - Listar Pilha.")
    print("0 - Sair.")
    OP = int(input("Entre com a opção desejada: "))
    if OP == 0:
        break
    elif OP == 1:
        if Pilha.PilhaCheia():
            print("Pilha Cheia")
        else:
            Valor = int(input("Entre com o valor a ser inserido: "))
            Pilha.PUSH(Valor)
    elif OP == 2:            
        if Pilha.PilhaVazia():
            print("Pilha Vazia")
        else:
            Valor = Pilha.POP()
            print("Valor %d retirado da pilha."%Valor)        
    elif OP == 3:
        if Pilha.PilhaVazia():
            print("Pilha Vazia")
        else:
            Pilha.ExibirLista()
        
    input("Digite uma tecla para continuar.")  