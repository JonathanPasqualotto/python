vet = []
for i in range(10):
    vet.append(int(input("Entre com o valor de vet[%d]:"%i)))
    
ima = 0
ime = 0

for i in range(1,10,1):
    if vet[i] > vet[ima]:
        ima = i
    if vet[i] < vet[ime]:
        ime = i

print("O menor valor encontrado foi %d e está no indice %d."%(vet[ime],ime))
print("O maior valor encontrado foi %d e está no indice %d."%(vet[ima],ima))
    

