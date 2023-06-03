import os
import time

tam = 10

class ClasseFila:
    def __init__(self):
        self.inicio = -1
        self.fim = -1
        self.fila = [0]*tam
    
    def FilaVazia(self):
        return self.inicio == -1 and self.fim == -1

    def FilaCheia(self):
        if self.fim + 1 == tam and self.inicio == 0:
            return True
        elif self.fim + 1 == self.inicio:
            return True
        else:
            return False
    
    def ENQUEUE(self,Valor):
        if self.FilaVazia():
            self.inicio += 1
            self.fim += 1
        else:
            self.fim += 1
            if self.fim == tam and self.inicio != 0:
                self.fim = 0
        self.fila[self.fim] = Valor

    def DEQUEUE(self):
        Valor = self.fila[self.inicio]
        if self.inicio == self.fim:
            self.inicio = -1
            self.fim = -1
        else:
            self.inicio += 1
            if self.inicio == tam and self.fim >= 0:
                self.inicio = 0
        return Valor

    def getINI(self):
        return self.inicio

    def getFIM(self):
        return self.fim

    def exibirLista(self):
        aux = self.inicio
        aux2 = self.fim
        while not self.FilaVazia():
            Valor = self.DEQUEUE()
            print('Valor %d retirado da fila\nInicio = %d\nFim = %d.'%(Valor,self.inicio,self.fim))
        self.inicio = aux
        self.fim = aux2

fila = ClasseFila()
while True:
    os.system('clear')
    valor = int(input('Digite um valor a ser inserido:\n'))
    if valor == 0:
        fila.exibirLista()
        time.sleep(2)
        exit()
    elif valor %2 == 0:
        fila.ENQUEUE(valor)
    elif valor %2 == 1:
        fila.DEQUEUE()
    
    input('Precisone uma telca para voltar...')
