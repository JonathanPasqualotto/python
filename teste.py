#recebe os dois valores na mesma linha
n = input().split()

#os valores assumem as variaveis na ordem como foram digitados
a, b = n

#condição iff para representar o item da tabela e determinar qual
#resultado exibido na tela
if a == '1':
    #dentro do comando formatt é feito o calculo usando a variavel
    #que recebeu o segundo valor "b" nesse caso uma multiplicação
    #o parametro ".2f" dentro do colchetes é para mostrar duas casas
    #depois da virgula..
    print('Total: R$ {:.2f}'.format(4.00*float(b)))
if a == '2':
    print('Total: R$ {:.2f}'.format(4.50*float(b)))
if a == '3':
    print('Total: R$ {:.2f}'.format(5.00*float(b)))
if a == '4':
    print('Total: R$ {:.2f}'.format(2.00*float(b)))
if a == '5':
 print('Total: R$ {:.2f}'.format(1.50*float(b)))