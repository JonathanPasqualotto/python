item = int(input('Item: '))
quant = int(input('Quantidade desse item: '))

if item == 1:
    print('Total: R$ {:.2f}'.format(4.00*int(quant)))
if item == 2:
    print('Total: R$ {:.2f}'.format(4.50*int(quant)))
if item == 3:
    print('Total: R$ {:.2f}'.format(5.00*int(quant)))
if item == 4:
    print('Total: R$ {:.2f}'.format(2.00*int(quant)))
if item == 5:
    print('Total: R$ {:.2f}'.format(1.50*int(quant)))
else:
    print("Item inválido!")