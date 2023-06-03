vet = []

for i in range(0,10,1):
    vet.append(int(input("Entre com o valor de vet[%d]:"%i)))

quant = 0
num = int(input("Entre com um número: "))
for i in range(10):
	if num == vet[i]:
	    quant+=1
print("O número %d foi encontrado %d vezes."%(num,quant))
