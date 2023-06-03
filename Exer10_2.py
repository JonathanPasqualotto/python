def LerVetor(vetor):
    #Entrada dos dados
    for i in range(10):
        vetor.append(int(input("Entre com o valor de vetor[%d]:"%i)))
    

vet1 = []
vet2 = []
vet3 = []
#Entrada dos dados
LerVetor(vet1)
LerVetor(vet2)
# Saída dos dados
for i in range(10):
    vet3.append(vet1[i] + vet2[i]) 
    
print(vet1)
print(vet2)
print(vet3)


