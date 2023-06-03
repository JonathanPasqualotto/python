dormir = 0
estudar = 0
passear = 0
ativ = 0

while True:
    print('O que voce mais gosta de fazer no findi.')
    print('1 - Dormir.')
    print('2 - Estudar algoritimos.')
    print('3 - Passear.')
    print('4 - Outros')
    print('5 - Estatisticas.')
    print('0 - Sair')
    opcao = input('Entre com a opção desejada: ')
    if opcao == '0':
        break
    if opcao == '1':
        dormir += 1
        print('\nEu gosto de dormir.\n')
    elif opcao == '2':
        estudar += 1
        print('\nEu gosto de estudar.\n')
    elif opcao == '3':
        passear += 1
        print('\nEu gosto de passear.\n')
    elif opcao == '4':
        ativ += 1
        print('\nEu gosto de qualquer outra atividade.\n')
    if opcao == '5':
        total = dormir + estudar + passear + ativ
        porcDorm = (dormir * 100) / total
        porcEst = (estudar * 100) / total
        porcPass = (passear * 100) / total
        porcAtiv = (ativ * 100) / total
        if dormir > estudar and dormir > passear and dormir > ativ:
            x = 'DORMIR'
            if estudar > dormir and estudar > passear and estudar > ativ:
                x = 'ESTUDAR'
                if passear > dormir and passear > estudar and passear > ativ:
                    x = 'PASSEAR'
                    if ativ > dormir and ativ > passear and ativ > estudar:
                        x = 'OUTRAS ATIVIDADES'
        else:
            x = 'EMPATE'
        print('\nESTATISTICAS')
        print('Foram um total de %d voto(s)'%total)
        print(' Para a opção 1 foram', dormir, 'voto(s)')
        print(' Para a opção 2 foram', estudar, 'voto(s)')
        print(' Para a opção 3 foram', passear, 'voto(s)')
        print(' Para a opção 4 foram', ativ, 'voto(s)')
        print('A porcentagem de votos para DORMIR foi de {:.1f}%'.format(porcDorm))
        print('A porcentagem de votos para ESTUDAR foi de {:.1f}%'.format(porcEst))
        print('A porcentagem de votos para PASSEAR foi de {:.1f}%'.format(porcPass))
        print('A porcentagem de votos para OUTRAS ATIVIDADES foi de {:.1f}%'.format(porcAtiv))
        print('A escolha com mais votos foi',x,'\n')