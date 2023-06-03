dia = int(input('Digite um dia qualquer entre 0 e 31: '))
mes = int(input('Digite um mês qualquer entre 1 e 12: '))
ano = int(input('Digite um ano qualquer: '))

if mes < 1 or mes > 12:
    print("Mês Inválido!")
else:
    if mes == 1:
        mes = 'Janeiro'
    elif mes == 2:
        mes = 'Fevereiro'
    elif mes == 3:
        mes = 'Março'
    elif mes == 4:
        mes = 'Abril'
    elif mes == 5:
        mes = 'Maio'
    elif mes == 6:
        mes = 'Junho'
    elif mes == 7:
        mes = 'Julho'
    elif mes == 8:
        mes = 'Agosto'
    elif mes == 9:
        mes = 'Semtembro'
    elif mes == 10:
        mes = 'Outubro'
    elif mes == 11:
        mes = 'Novembro'
    elif mes == 12:
        mes = 'Dezembro'
    print('Chapecó, %s / %s / %s'%(dia,mes,ano))

