num = int(input('Digite o número a ser encontrado: '))
achou = False
for i in range(0, 10):
    num2 = int(input('Digite um número: '))
    if num2 == num:
        achou = True
if achou:
    print('NUMERO ENCONTRADO')
else:
    print('NUMERO NÃO ENCONTRADO')
