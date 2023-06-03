import time
import os
n1 = int(input('QUANTOS ALNOS TEM NA TURMA DE SISTEMAS DE INFORMAÇÃO\n'))
n2 = int(input('QUANTOS ALNOS TEM NA TURMA DE ENGENHARIA DA COMPUTAÇÃO\n'))
totalAcad = n1 + n2
totalSis = n1
totalEng = n2
SisInfo = 0
EngComp = 0
while True:
    os.system("clear")
    print('     QUAL TURMA VOCÊ FAZ PARTE?\n')
    print('41 - SISTEMAS DE INFORMAÇÃO')
    print('620 - ENGENHARIA DA COMPUTAÇÃO')
    print('0 - SAIR\n')
    opcao = int(input('OPÇÃO: '))

    if opcao == 41:
        print('ALUNO DE SISTEMAS DE INFORMAÇÃO\n')
        SisInfo += 1
    elif opcao == 620:
        print('ALUNO DE ENGENHARIA DA COMPUTAÇÃO\n')
        EngComp += 1
    elif opcao == 0:
        totalResp = SisInfo + EngComp
        porcSis = (SisInfo / totalSis) * 100
        porcEng = (EngComp / totalEng) * 100
        faltSis = totalSis - SisInfo
        faltEng = totalEng - EngComp
        porcFaltSis = (faltSis / totalSis) * 100
        porcFaltEng = (faltEng / totalEng) * 100
        if porcSis > porcEng:
            x = 'SISTEMAS DE INFORMAÇÃO!!!'
        elif porcEng > porcSis:
            x = 'ENGENHARIA DA COMPUTAÇÃO!!!'
        else:
            x = 'DEU EMPATE!'
        print('TOTAL DE ACADÊMICOS QUE RESPONDERAM FOI:', totalAcad)
        print('TOTAL DE ACADÊMICOS DE CADA CURSO:\nSisInfo:',SisInfo,'\nEngComp:',EngComp)
        print('PORCENTAGEM DE PARTICIPAÇÃO DE CADA CURSO:\nSisInfo: {:.2f}%\nEngComp: {:.2f}%'.format(porcSis,porcEng))
        print('O TOTAL DE FALTANTES PARA CADA CURSO FOI:\nSisInfo: Total {}, Correspondem à {:.2f}%\nEngComp: Total {}, Correspondem à {:.2f}%'.format(faltSis,porcFaltSis,faltEng,porcFaltEng))
        print('O CURSO QUE TEVE MAIS PARTICIPAÇÃO FOI:\n',x)
        break
    else:
        print('OPÇÃO INVÁLIDA!\n')
        time.sleep(1)
        continue
    time.sleep(1)