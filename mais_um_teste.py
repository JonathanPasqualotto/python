import os
os.system('clear')

contador = 0
def ordena(vetor):
    global contador
    i = 0
    for i in range(len(vetor)):
        if vetor[i] == vetor[i-1]:
            contador += 1

while True:
    vetor = list(map(int,input().split()))
    if 0 in vetor:
        break
    vet = ordena(vetor)
    print(contador)
    if contador % 2 == 0:
        print ('Carlos')
        contador = 0
    else:
        print ('Marcelo')
        contador = 0