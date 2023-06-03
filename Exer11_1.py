vet = []
flag = [0]*10
contar = 0
for i in range(0,10,1):
    vet.append(int(input("Entre com o valor de vet[%d]: "%i)))

num = int(input("Entre com um valor: "))
for i in range(0,10,1):
    if vet[i] == num:
        flag[i] = 1
        contar = contar + 1
print("O número %d foi encontrado %d vezes.\nNo indices: "%(num,contar))
for i in range(0,10,1):
    if flag[i] == 1:
        print("%d "%i,end = '')