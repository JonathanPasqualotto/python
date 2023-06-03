import os
os.system('clear')

minimo = 9999999999
n = int(input())
pilha = []
for i in range(n):
    texto = input()
    if texto == 'MIN':
        if not pilha:
            print('EMPTY')
        else:
            minimo = min(pilha)
            print(minimo)
    elif texto == 'POP':
        if not pilha:
            print('EMPTY')
        else:
            valor = pilha.pop()
            if minimo == valor:
                if not pilha:
                    minimo = 9999999999
                else:
                    minimo = min(pilha)
    else:
        comando,valor = texto.split()
        valor = int(valor)
        pilha.append(valor)
