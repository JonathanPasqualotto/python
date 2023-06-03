contador = 0
def ordena(vetor, indice):
    global contador
    aux = indice
    i = int(len(vetor))
    for i in range(len(vetor)):
        if vetor[aux] < vetor[aux-1]:
            temp = vetor[aux]
            vetor[aux] = vetor[aux-1]
            vetor[aux-1] = temp
            aux -= 1
            contador += 1
            if aux == 0:
                break
    if indice < len(vetor)-1:
        ordena(vetor, indice+1)

while True:
    vetor = list(map(int,input().split()))
    if 0 in vetor:
        break
    vetor.pop(0)
    vet = ordena(vetor, 1)
    if contador % 2 == 0:
        print ('Carlos')
        contador = 0
    else:
        print ('Marcelo')
        contador = 0