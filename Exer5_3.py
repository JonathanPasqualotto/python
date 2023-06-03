dia = int(input('Digite um dia qualquer entre 0 e 31: '))
mes = int(input('Digite um mês qualquer entre 1 e 12: '))
ano = int(input('Digite um ano qualquer: '))
dic = {1:'Janeiro',2:'Fevereiro',3:'Março',4:'Abril',5:'Maio',6:'Junho',7:'Julho',8:'Agosto',9:'Semtembro',10:'Outubro',11:'Novembro',12:'Dezembro'}

print('Chapecó, %s / %s / %s'%(dia,dic[mes],ano))