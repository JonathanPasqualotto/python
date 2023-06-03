import os
import time

jogador1 = None
jogador2 = None
jogadas = 0

''' AQUI É CHECADO SE O VALOR QUE É DIGITADO É VALIDO
    NADA É ACEITO ALÉM DOS NUMEROS 1 E 0'''
def opcaoMenu():
    global opcao
    while True:
        opcao = input('Opção: ')
        try:
            opcao = int(opcao)
            if opcao == 1 or opcao == 0:
                return opcao
            else:
                print('Opção Inválida!')
                print('Digite um número entre (0 e 1)')
                time.sleep(2)
        except ValueError:  # EXCEÇÃO DE VALOR ERRADO NADA ACEITO ALEM DOS NUMERO INFORMADOS NO IF
            print('Isto não é um número válido entre 0 e 1. Tente novamente.')
            time.sleep(2)
            continue

def Iniciar():
    print('''
                 #-#-#-#-#-#-#-#-#-#-#-#-#-#-#
                 #                           #
                 #      BEM VINDO AO JOGO    #
                 #         TIC TAC TOE       #  
                 #                           #
                 #-#-#-#-#-#-#-#-#-#-#-#-#-#-#''')
    print('''
    #-#-#-#-#-#-#-#-#-#-#-#-#-#-#
    #  SELECIONE UMA OPÇÃO      #
    #                           #
    # 1 - INICIAR GAME          #
    # 0 - SAIR                  #
    #-#-#-#-#-#-#-#-#-#-#-#-#-#-#\n''')
    opcaoMenu()

    if opcao == 1:
        Menu()
    elif opcao == 0:
        os.system('clear')
        print('Obrigado por Jogar Tic Tac Toe...')
        print('Até o proximo jogo..')
        time.sleep(2)
        exit()

    else:
        print('Opção Inválida!')
        Iniciar()


def Menu():
    # DEVEM SER DECLARADAS AS VARIAVEIS GLOBAIS PARA QUE POSSAM SER USADAS
    # NAS DEMAIS FUNÇÕES DO GAME
    global jogador1, jogador2
    os.system('clear')
    print('Qual é o nome do Jogador 1: ?')
    jogador1 = input()
    print('Qual é o nome do Jogador 2: ?')
    jogador2 = input()
    Game()

# CHECA SE É NUMERO VALIDO
def linhaColuna():
    global linha, coluna
    while True:
        linha = input('Linha: ')
        coluna = input('Coluna: ')
        try:
            linha = int(linha)
            coluna = int(coluna)
            if linha < 4 and coluna < 4:
                return linha, coluna
            else:
                print('Algum número invalido!')
                print('Escolha outro..')
                time.sleep(2)
        except ValueError:
            print('Isto não é um número válido de 1 à 3. Tente novamente.')
            time.sleep(2)
            continue

def Game():
    global jogadas

    # LOOP PRINCIPAL DO GAME
    while Ganhou() == 0:
        os.system('clear')
        if (jogadas % 2 +1) == 1:           # ESSA DIVISÃO É PARA SABER DE QUEM É O JOGADOR DA VEZ
            print('Jogador ',jogador1)
            print('Escolha um número de (1 à 3)')
        else:
            print('Jogador ',jogador2)
            print('Escolha um número de (1 à 3)')

        Tabuleiro()         # É CHAMADA A EXIBIÇÃO DO TABULEIRO
        linhaColuna()       # RECEBENDO O VALOR DE LINHA E COLUNA

        # ONDE A MAGICA ACONTECE
        # AQUI É ADICIONADO 1 E -1 NOS LUGARES ESCOLHIDOS PELOS JOGADORES
        if velha[linha-1][coluna-1] == 0:
            if (jogadas%2+1) == 1:
                velha[linha-1][coluna-1] = 1
            else:
                velha[linha-1][coluna-1] = -1
        else:
            os.system('clear')
            print('Esta posição esta sendo ocupada')
            print('Escolha outra..')
            time.sleep(2)
            jogadas -=1

        if Ganhou():
            os.system('clear')
            Tabuleiro()
            if (jogadas % 2 + 1) == 1:
                print('\nJogador ', jogador1, " ganhou apos ", jogadas + 1, " rodadas")
                time.sleep(3)
                novoGame()
            else:
                print('\nJogador ', jogador2, " ganhou apos ", jogadas + 1, " rodadas")
                time.sleep(3)
                novoGame()
        jogadas += 1

def Ganhou():
    # CHECAR AS LINHAS
    for i in range(3):
        check = velha[i][0] + velha[i][1] + velha[i][2]
        if check == 3 or check == -3:
            return 1

    # CHECAR AS COLUNAS
    for i in range(3):
        check = velha[0][i] + velha[1][i] + velha[2][i]
        if check == 3 or check == -3:
            return 1

    # CHECAR AS DIAGONAIS
    check1 = velha[0][0] + velha[1][1] + velha[2][2]
    check2 = velha[0][2] + velha[1][1] + velha[2][0]
    if check1 == 3 or check1 == -3 or check2 == 3 or check2 == -3:
        return 1

    ''' CHECANDO EMPATE
        SE O NUMERO DE JOGADAS FOR NOVE E NAO TEVE NENHUM GANHADOR É EMPATE'''
    if jogadas == 9:
        os.system('clear')
        print('''\n
        #-#-#-#-#-#-#-#
        #  Deu VELHA  #
        #-#-#-#-#-#-#-#''')
        Tabuleiro()
        time.sleep(3)
        zerarTabuleiro()
        novoGame()
        return 1

    return 0

# IMPRIME O TABULEIRO
def Tabuleiro():
    print()  # UMA LINHA EM BRANCO ACIMA
    for i in range(3):
        for j in range(3):
            if velha[i][j] == 0:
                print('''   |_|''', end=' ')
            elif velha[i][j] == 1:
                print('''   |X|''', end=' ')
            elif velha[i][j] == -1:
                print('''   |O|''', end=' ')

        print() # UMA LINHA PARA MANTER A ORDEM CORRETA DO TABULEIRO
    print() # UMA LINHA EM BRANCO A BAIXO


def opcaoMenuNovo():
    global opcaon
    while True:
        opcaon = input('Opção: ')
        try:
            opcaon = int(opcaon)
            if opcaon == 1 or opcaon == 0:
                return opcaon
            else:
                print('Opção Inválida!')
                print('Digite um número entre (0 e 1)')
                time.sleep(2)
        except ValueError:
            print('Isto não é um número válido entre 0 e 1. Tente novamente.')
            time.sleep(2)
            continue
'''AQUI INICIA UM NOVO JOGO'''
def novoGame():
    global jogadas
    print('''
        #-#-#-#-#-#-#-#-#-#-#-#-#-#-#
        #     Deseja Jogar          #
        #      Novamente?           #
        # 1 - Sim                   #  
        # 0 - Não                   #
        #-#-#-#-#-#-#-#-#-#-#-#-#-#-#\n''')
    opcaoMenuNovo()
    #opcao = int(input('Opção: '))

    if opcaon == 1:
        jogadas = 0          # ZERA O NUMERO DE JOGADAS, POIS É REFERENCIA PARA SABER QUEM É A VEZ DE JOGAR E SE DEU EMPATE
        zerarTabuleiro()     # CHAMA FUNÇÃO PARA ZERAR O TABULEIRO
        time.sleep(3)
        Game()
    else:
        os.system('clear')
        print('Obrigado por Jogar Tic Tac Toe...')
        print('Até o proximo jogo..')
        time.sleep(2)
        exit()

'''FUNÇÃO PARA ZERAR O TABULEIRO
    ONDE ENCONTRAR OS NUMEROS 1 E -1 É SUBSTITUIDO POR 0'''
def zerarTabuleiro():
    for i in range(3):
        for j in range(3):
            if velha[i][j] == 1 or velha[i][j] == -1:
                velha[i][j] = 0



''' ISSO É UMA MATRIZ EM PYTHON
    CONHECIDO COMO BOARD TAMBEM, SÃO DOIS COLCHETES UM DENTRO DO OUTRO SEPARADOS POR UMA VIRGULA, NESSA COLOCAÇÃO É FORMADA UMA MATRIZ DE 3 POR 3, 
    MAS PODE SER FEITA UMA MATRIZ O JEITO QUE QUISER DESDE QUE SIGA O MODELO "[[0]]" '''
velha= [ [0,0,0],
         [0,0,0],
         [0,0,0] ]

Iniciar()


