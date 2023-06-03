import os

os.system('clear')


contador = 0
def ordem(vetor):
    global contador
    for i in range(len(vetor)): 
        if vetor[i] > vetor[i-1]:     
            contador += 1
        #if vetor[i] > vetor[i-1] and vetor[i] > vetor[i+1]:
        #    contador += 1
    return vetor
            


while True:
    vetor = list(map(int,input().split()))
   # print(vetor.sort())
   # print(len(vetor))
    if vetor == 0:
        break
    vet = ordem(vetor)
    print(vet)
    print(contador)
    if (contador % 2) == 0:
        print ('Carlos')
        contador = 0
    else:
        print ('Marcelo')
        contador = 0