from unittest import result


def Menu():
    x = float(input('Digite o valor a ser convertido: '))
    dolar = convertDolar(x)
    real = convertReal(x)
    print('Valor em dolares: {:.2f}'.format(dolar))
    print('Valor em reais: {:.2f}'.format(real))

def convertDolar(val):
    resultado = val * 5.11
    return resultado

def convertReal(val):
    resultado = val / 5.11
    return resultado

Menu()