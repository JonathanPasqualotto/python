vet = []


def LerVetor(vetor):
    for i in range(10):
        vetor.append(int(input("Entre com o valor de vet[%d]:" % i)))


def MostrarVetor(vetor):
    for i in reversed(vetor):
        print(i)


LerVetor(vet)

MostrarVetor(vet)
