base = int(input('Digite um valor para a base: '))
expoente = int(input('Digite um valor para o expoente: '))
potencia = 1
i = 1
while i <= expoente:
    potencia *= base
    i += 1
print('O valor da portencia é = %d'%potencia)