def DeterminaNumero(num):
    if num > 0:
        return 'Positivo'
    elif num < 0:
        return 'Negativo'
    else:
        return 'Zero'

n = int(input('Ente com o número: '))
print('O numero %d é %s'%(n,DeterminaNumero(n)))