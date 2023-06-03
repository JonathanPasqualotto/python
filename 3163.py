def Coordenadas(posicao,entrada):
    if posicao == '-1':
        oeste.append(entrada)
    elif posicao == '-2':
        sul.append(entrada)
    elif posicao == '-3':
        norte.append(entrada)
    else:
        leste.append(entrada)

def OrdemNaves():
    aux = True
    while len(leste) != 0 or len(norte) != 0 or len(oeste) != 0 or len(sul) != 0:
        if len(oeste) > 0:
            filaPrincipal.append(oeste.pop(0))
        
        if len(norte) > 0:
            if aux:
                filaPrincipal.append(norte.pop(0))
                aux = False
        
        if len(sul) > 0:
            filaPrincipal.append(sul.pop(0))
            aux = True
        
        if len(leste) > 0:
            filaPrincipal.append(leste.pop(0))

    print(filaPrincipal)


leste = []
norte = []
sul = []
oeste = []
filaPrincipal = []
while True:
    entrada = input()
    if entrada == '0':
        OrdemNaves()
        break
    elif entrada in ('-1','-2','-3','-4'):
        posicao = entrada
    else:
        Coordenadas(posicao,entrada)