import os
import time

saldoCaixa = 0
diaAnterior = 0
val = 0
urso = 0
carroEletrico = 0
caminhao = 0
c4x4 = 0
resul = 0
nome = None

def Inicio():
    global diaAnterior, nome
    print('''
             #-#-#-#-#-#-#-#-#-#-#-#-#-#-#
             #                           #
             #   BEM VINDO A PLAYKIDS    #
             #                           #
             #-#-#-#-#-#-#-#-#-#-#-#-#-#-#\n''')
    print('Qual é seu nome?')
    nome = input()
    print("O saldo atual é de: {:.2f}".format(saldoCaixa))
    print('Qual foi o valor vendido no dia anteriro? ')
    diaAnterior = float(input())
    Menu()

def opcaoMenu():
    global opcao
    while True:
        opcao = input('Opção: ')
        try:
            opcao = int(opcao)
            if opcao <= 4:
                return opcao
            else:
                print('Opção Inválida!')
                print('Digite um número entre (1 e 4)')
                time.sleep(2)
        except ValueError:  # EXCEÇÃO DE VALOR ERRADO NADA ACEITO ALEM DOS NUMERO INFORMADOS NO IF
            print('Isto não é um número válido entre 1 e 4. Tente novamente.')
            time.sleep(2)
            continue
def Menu():
    global diaAnterior, saldoCaixa
    os.system('clear')
    print('''
             #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
             #                            #
             #   ESCOLHA UMA OPÇÃO        #
             #                            #
             # 1 - INICIAR BRINCADEIRA    #
             # 2 - FINALIZAR BRINCADEIRA  #
             # 3 - VENDA DE PRODUTOS      #
             # 4 - FECHAR O CAIXA         #
             #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-\n''')
    opcaoMenu()

    if opcao == 1:
        iniciarBrincadeira()
    if opcao == 2:
        finalizaBrincadeira()
    if opcao == 3:
        vendaProduto()
    if opcao == 4:
        fecharCaixa()

def fecharCaixa():
    global saldoCaixa, val, urso, carroEletrico, caminhao, c4x4, diaAnterior, nome
    os.system('clear')
    print('''
                 #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
                 #      FECHAMENTO DO CAIXA    #
                 #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-\n''')
    print('%s, Aqui temos o resumo de seu dia de trabalho\n'%nome)
    print('Total movimentado no dia é de: R$: {:.2f}'.format(saldoCaixa))
    print('Quantia recebida de locação dos Ursos: R$ {:.2f}'.format(urso))
    print('Quantia recebida de locação dos Carros: R$ {:.2f}'.format(carroEletrico))
    print('Quantia recebida de locação dos Caminhões e 4x4: R$ {:.2f}'.format(caminhao + c4x4))
    print('Quantia recebido em produtos vendidos: R$ {:.2f}'.format(val))
    print('Percentual de diferença da entrada atual e do dia anterior: {:.2f}%'.format((saldoCaixa - diaAnterior)*100/diaAnterior))
    time.sleep(3)
    exit()



def opcaoMenu2():
    global opcao2
    while True:
        opcao2 = input('Opção: ')
        try:
            opcao2 = int(opcao2)
            if opcao2 <= 5:
                return opcao2
            else:
                print('Opção Inválida!')
                print('Digite um número entre (1 e 5)')
                time.sleep(2)
        except ValueError:  # EXCEÇÃO DE VALOR ERRADO NADA ACEITO ALEM DOS NUMERO INFORMADOS NO IF
            print('Isto não é um número válido entre 1 e 5. Tente novamente.')
            time.sleep(2)
            continue
# A empresa possuí 3 Ursos, 3 Carros Elétricos e 3 Caminhões e 4x4
lib = [[0,0,0]]
lib1 = [[0,0,0]]
lib2 = [[0,0,0]]
lib3 = [[0,0,0]]
def iniciarBrincadeira():
    global saldoCaixa, urso, carroEletrico, caminhao, c4x4
    os.system('clear')
    print('''
             #-#-#-#-#-#-#-#-#-#-#-#-#-#-#
             #                           #
             #   QUAL BRINQUEDO VOCÊ     #
             #      DESEJA UTILIZAR      #
             #                           #
             # 1 - URSO                  #
             # 2 - CARRO ELÉTRICO        #
             # 3 - CAMINHÃO              #
             # 4 - 4x4                   #
             # 5 - VOLTAR PARA O MENU    #
             #-#-#-#-#-#-#-#-#-#-#-#-#-#-#\n''')
    opcaoMenu2()

    if opcao2 == 1:
        if lib[0][0] == 1 and lib[0][1] == 1 and lib[0][2] == 1:
            print('Brinquedos OCUPADOS!\nDeve aguardar o retorno dos mesmos.')
            time.sleep(2)
            iniciarBrincadeira()
        else:
            for i in range(3):
                if lib[0][i] == 0:
                    lib[0][i] = 1
                    urso += 25.00
                    saldoCaixa += urso
                    print('Brinquedo locado')
                    time.sleep(2)
                    iniciarBrincadeira()

    if opcao2 == 2:
        if lib1[0][0] == 1 and lib1[0][1] == 1 and lib1[0][2] == 1:
            print('Brinquedos OCUPADOS!\nDeve aguardar o retorno dos mesmos.')
            time.sleep(2)
            iniciarBrincadeira()
        else:
            for i in range(3):
                if lib1[0][i] == 0:
                    lib1[0][i] = 1
                    carroEletrico += 30.00
                    saldoCaixa += carroEletrico
                    print('Brinquedo locado')
                    time.sleep(2)
                    iniciarBrincadeira()

    if opcao2 == 3:
        if lib2[0][0] == 1 and lib2[0][1] == 1 and lib2[0][2] == 1:
            print('Brinquedos OCUPADOS!\nDeve aguardar o retorno dos mesmos.')
            time.sleep(2)
            iniciarBrincadeira()
        else:
            for i in range(3):
                if lib2[0][i] == 0:
                    lib2[0][i] = 1
                    caminhao += 35.00
                    saldoCaixa += caminhao
                    print('Brinquedo locado')
                    time.sleep(2)
                    iniciarBrincadeira()

    if opcao2 == 4:
        if lib3[0][0] == 1 and lib3[0][1] == 1 and lib3[0][2] == 1:
            print('Brinquedos OCUPADOS!\nDeve aguardar o retorno dos mesmos.')
            time.sleep(2)
            iniciarBrincadeira()
        else:
            for i in range(3):
                if lib3[0][i] == 0:
                    lib3[0][i] = 1
                    c4x4 += 35.00
                    saldoCaixa += c4x4
                    print('Brinquedo locado')
                    time.sleep(2)
                    iniciarBrincadeira()

    if opcao2 == 5:
        Menu()


def brinquedosOcupados():
    ursoocupado = 0
    carroocupado = 0
    caminhaoocupado = 0
    c4x4ocupado = 0
    for i in range(3):
        if lib[0][i] == 1:
            ursoocupado += 1

    for i in range(3):
        if lib1[0][i] == 1:
            carroocupado += 1

    for i in range(3):
        if lib2[0][i] == 1:
            caminhaoocupado += 1

    for i in range(3):
        if lib3[0][i] == 1:
            c4x4ocupado += 1

    print('''
             #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
             #                                    #
             #   Resumo dos Brinquedos Ocupados   #
             #                                    #
             #  Ursos Ocupados: %s                 #
             #  Carros Elétricos Ocupados: %s      #
             #  Caminhões ocupados: %s             #
             #  4x4 ocupados: %s                   #
             #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-'''%(ursoocupado, carroocupado, caminhaoocupado, c4x4ocupado))

def opcaoMenu3():
    global opcao3
    while True:
        opcao3 = input('Opção: ')
        try:
            opcao3 = int(opcao3)
            if opcao3 <= 5:
                return opcao3
            else:
                print('Opção Inválida!')
                print('Digite um número entre (1 e 5)')
                time.sleep(2)
        except ValueError:  # EXCEÇÃO DE VALOR ERRADO NADA ACEITO ALEM DOS NUMERO INFORMADOS NO IF
            print('Isto não é um número válido entre 1 e 5. Tente novamente.')
            time.sleep(2)
            continue

def opcaoNum3():
    global num3
    while True:
        num3 = input('Opção: ')
        try:
            num3 = int(num3)
            if num3 <= 5:
                return num3
            else:
                print('Opção Inválida!')
                print('Digite um número entre (0 e 2)')
                time.sleep(2)
        except ValueError:  # EXCEÇÃO DE VALOR ERRADO NADA ACEITO ALEM DOS NUMERO INFORMADOS NO IF
            print('Isto não é um número válido entre 0 e 2. Tente novamente.')
            time.sleep(2)
            continue

def finalizaBrincadeira():
    os.system('clear')
    brinquedosOcupados()
    print('''
             #-#-#-#-#-#-#-#-#-#-#-#-#-#-#
             #   QUAL BRINQUEDO DESEJA   #
             #         FINALIZAR         #
             #                           #
             # 1 - URSO                  #
             # 2 - CARRO ELÉTRICO        #
             # 3 - CAMINHÃO              #
             # 4 - 4x4                   #
             # 5 - VOLTAR AO MENU        #
             #-#-#-#-#-#-#-#-#-#-#-#-#-#-#\n''')
    opcaoMenu3()

    if opcao3 == 1:
        os.system('clear')
        print('QUAL É O CÓDIGO DO URSO PARA FINALIZAR(0-2)?')
        opcaoNum3()
        if lib[0][num3] == 1:
            lib[0][num3] = 0
            print('Brinquedo Finalizado')
            time.sleep(3)
            finalizaBrincadeira()
        else:
            print('Este URSO não está sendo utilizado')
            time.sleep(3)
            finalizaBrincadeira()

    if opcao3 == 2:
        os.system('clear')
        print('QUAL É O CÓDIGO DO CARRO ELÉTRICO PARA FINALIZAR(0-2)?')
        opcaoNum3()
        if lib1[0][num3] == 1:
            lib1[0][num3] = 0
            print('Brinquedo Finalizado')
            time.sleep(3)
            finalizaBrincadeira()
        else:
            print('Este CARRO ELÉTRICO não está sendo utilizado')
            time.sleep(3)
            finalizaBrincadeira()


    if opcao3 == 3:
        os.system('clear')
        print('QUAL É O CÓDIGO DO CAMINHÃO PARA FINALIZAR(0-2)?')
        opcaoNum3()
        if lib2[0][num3] == 1:
            lib2[0][num3] = 0
            print('Brinquedo Finalizado')
            time.sleep(3)
            finalizaBrincadeira()
        else:
            print('Este CAMINHÃO não está sendo utilizado')
            time.sleep(3)
            finalizaBrincadeira()

    if opcao3 == 4:
        os.system('clear')
        print('QUAL É O CÓDIGO DO 4x4 PARA FINALIZAR(0-2)?')
        opcaoNum3()
        if lib3[0][num3] == 1:
            lib3[0][num3] = 0
            print('Brinquedo Finalizado')
            time.sleep(3)
            finalizaBrincadeira()

        else:
            print('Este 4x4 não está sendo utilizado')
            time.sleep(3)
            finalizaBrincadeira()

    if opcao3 == 5:
        Menu()

def vendaProduto():
    global saldoCaixa, val
    os.system('clear')
    print('Digite o valor da venda realizada: ')
    valor = float(input())
    val += valor
    saldoCaixa += valor
    Menu()




Inicio()