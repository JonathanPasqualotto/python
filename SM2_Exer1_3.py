def calculaConta(val,perc):
    gorjeta = val * (perc/100.0)
    total = val + gorjeta
    print('Consumo %0.2f'%val)
    print('Gorjeta de %0.2f = %0.2f'%(perc,gorjeta))
    print('Valor total = %0.2f'%total)

x = float(input('Entre com o valor consumido: '))
y = float(input('Entre com o %% de serviço: '))
calculaConta(x,y)