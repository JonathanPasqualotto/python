vet = []

def Menu():
    print('''
    1 - Cadastrar Vetor
    2 - Remove Vetor
    3 - Exibir Vetor
    4 - Exibir Vetor de Traz/Frente
    5 - Procurar por Valor
    6 - Procurar por Indice
    7 - Sair''')

    opcao = int(input('Opção: '))
    
    if opcao == 1:
        CadastrarVetor()
    if opcao == 2:
        RemoveVetor()
    if opcao == 3:
        ExibeVetor()
    if opcao == 4:
        TrazFrente()
    if opcao == 5:
        ProcuraValor()
    if opcao == 6:
        ProcuraIndice()
    if opcao == 7:
        exit()


def CadastrarVetor():
    if len(vet) == 9:
        print('O vetor esta cheio')
        Menu()
    else:
        vet.append(int(input('Entre com o valor no indice %d'%len(vet))))
        Menu()

def RemoveVetor():
    if not vet:
        print('O vetor esta vazio')
        Menu()
    else:
        print('o valor retirado foi: %d'%vet.pop())
        Menu()


def ExibeVetor():
    print(vet)
    Menu()


def TrazFrente():
    print(vet[::-1])
    Menu()


def ProcuraValor():
    x = int(input('Digite o valor à ser encontrado: '))
    if x in vet:
       print('Numero encontrado: ',x)
       Menu()
    else:
        print('Valor nao encontrado')
        Menu()



def ProcuraIndice():
    x = int(input('Digite o valor do indice: '))
    if x < 0 or x > len(vet):
        print('Indice Incorreto')
        Menu()
    else:
        print('o valor no indice %d = %d'%(x,vet[x]))
        Menu()




Menu()



