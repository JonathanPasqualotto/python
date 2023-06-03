def calcula(n):
    s = 1.0
    for i in range(2,n+1,1):
        s = s + (1.0/i)
    return s

n = int(input('Entre com o valor: '))
s = calcula(n)
print('o valor de S para %d = %0.4f'%(n,s))
