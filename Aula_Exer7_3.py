base = int(input("Digite um valor para a base: "))
expoente = int(input("Digite um valor para o expoente: "))
potencia = 1
for i in range(expoente):
    potencia *= base
    i += 1
print('A potencia é:',potencia)