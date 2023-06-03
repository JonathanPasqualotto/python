def LeVetor(vet):
    for i in range(0,10,1):
        vet.append(input('Entre com o valor do indice %d: '%i))

def Troca(vetIni, vetAtu):
    for i in range(10):
        vetIni[i] = vetAtu[i]

def VerIncorretos(vetIni, vetAtu):
    Incorretos = 0
    for i in range(10):
        if vetIni[i] == vetAtu[i]:
            Incorretos += 1

        return Incorretos

vetIni = []
print('Entre com oarquivo inicial a ser testado: ')
LeVetor(vetIni)

while True:
    codigoAtu = int(input('Código da atualização: '))
    if codigoAtu == 0:
        break
    print('Digite os indices do arquivo a ser atualizado: ')
    vetAtu = []
    LeVetor(vetAtu)
    if VerIncorretos(vetIni,vetAtu) == 10:
        print('NÃO SERÁ POSSIVEL ATUALIZAR PORQUE DEVERA REALIZAR MERGE')
    else:
        Troca(vetIni,vetAtu)
        print('ARQUIVO ATUALIZADO')