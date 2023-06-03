import time
import os

''' AQUI É CHECADO SE O VALOR QUE É DIGITADO É VALIDO
    NADA É ACEITO ALÉM DOS NUMEROS ENTRE 0 E 5'''
def opcaoMenu():
    global opcao
    while True:
        opcao = input('Opção: ')
        try:
            opcao = int(opcao)
            if opcao <= 5:
                return opcao
            else:
                print('Opção Inválida!')
                print('Digite um número entre (0 e 5)')
                time.sleep(2)
        except ValueError:  # EXCEÇÃO DE VALOR ERRADO NADA ACEITO ALEM DOS NUMERO INFORMADOS NO IF
            print('Isto não é um número válido entre 0 e 5. Tente novamente.')
            time.sleep(2)
            continue
def Menu():
    os.system('clear')
    print('''
    #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
    #     BEM VINDO AO CLOSETUSE    #
    #                               #
    # 1 - SITUAÇÃO DOS ARMÁRIOS     #
    # 2 - ARMÁRIOS LIVRES           #
    # 3 - UTILIZAR ARMÁRIO          #
    # 4 - REMOVER ARMÁRIO           #
    # 5 - RESUMO DOS ARMÁRIOS       #
    # 0 - SAIR                      #
    #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#\n''')
    opcaoMenu()
    #opcao = int(input("Escolha uma opção: "))

    if opcao == 0:
        Sair()
    elif opcao == 1:
        situacaoArmarios()
    elif opcao == 2:
        armariosLivres()
    elif opcao == 3:
        utilizarArmario()
    elif opcao == 4:
        removerArmario()
    elif opcao == 5:
        resumoArmario()


def Sair():
    os.system('clear')
    print('Aproveite o Armário!\n')
    print('A UNOESC Agradece a sua Confiança...')
    time.sleep(2)
    exit()


def situacaoArmarios():
    os.system('clear')
    for i in range(1):
        for j in range(10):
            if board[i][j] == 0:
                print('Armario %d LIVRE!\n' %j)
            elif board[i][j] == 1:
                print('Armario %d OCUPADO!\n'%j)
    time.sleep(3)
    Menu()


def armariosLivres():
    os.system('clear')
    for j in range(10):
        if board[0][j] == 0:
            print('Armario %d LIVRE!\n' %j)
    time.sleep(5)
    Menu()

def opcaoUtiliza():
    global num
    while True:
        num = input('Opção: ')
        try:
            num = int(num)
            if num <= 9:
                return num
            else:
                print('Opção Inválida!')
                print('Digite um número entre (0 e 9)')
                time.sleep(2)
        except ValueError:  # EXCEÇÃO DE VALOR ERRADO NADA ACEITO ALEM DOS NUMERO INFORMADOS NO IF
            print('Isto não é um número válido entre 0 e 9. Tente novamente.')
            time.sleep(2)
            continue

def utilizarArmario():
    os.system('clear')
    print('Informe o Número do Armário que deseja utilizar(0-9)? ')
    opcaoUtiliza()
    for j in range(10):
        if board[0][j] == board[0][num]:
            board[0][num] = 1
            print('O Armário agora é seu, bom aproveito!')
            time.sleep(3)
            Menu()
            break
        else:
            print('ARMÁRIO SENDO UTILIZADO!')
            print('Escolha outro número!')
            time.sleep(3)
            utilizarArmario()
            break

def opcaoUtiliza2():
    global num2
    while True:
        num2 = input('Opção: ')
        try:
            num2 = int(num2)
            if num2 <= 9:
                return num2
            else:
                print('Opção Inválida!')
                print('Digite um número entre (0 e 9)')
                time.sleep(2)
        except ValueError:  # EXCEÇÃO DE VALOR ERRADO NADA ACEITO ALEM DOS NUMERO INFORMADOS NO IF
            print('Isto não é um número válido entre 0 e 9. Tente novamente.')
            time.sleep(2)
            continue

def removerArmario():
    os.system('clear')
    print('Informe o Número do Armário que deseja remover(0-9)? ')
    opcaoUtiliza2()
    if board[0][num2] == 1:
        board[0][num2] = 0
        print('O Armário foi removido com sucesso!')
        time.sleep(3)
        Menu()

    else:
        print('ARMÁRIO NÃO ESTÁ SENDO UTILIZADO!')
        print('Escolha outro número!')
        time.sleep(3)
        removerArmario()

def resumoArmario():
    os.system('clear')
    livre = 0
    ocupado = 0
    for i in range(10):
        if board[0][i] == 0:
            livre += 1
        elif board[0][i] == 1:
            ocupado += 1
    print('''
          %d Armário(s) LIVRE(S)
          %d Armário(s) OCUPADO(S)'''%(livre,ocupado))
    time.sleep(3)
    Menu()

''' ISSO É UMA MATRIZ EM PYTHON
    CONHECIDO COMO BOARD TAMBEM, SÃO DOIS COLCHETES UM DENTRO DO OUTRO SEPARADOS POR UMA VIRGULA, NESSA COLOCAÇÃO É FORMADA UMA MATRIZ DE 1 POR 10, 
    MAS PODE SER FEITA UMA MATRIZ O JEITO QUE QUISER DESDE QUE SIGA O MODELO "[[0]]" 
    Aonde borad = [i][j] primeiro [i] é linha e o outro [j] coluna '''

board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

Menu()