nome = input('Digite seu nome: ')
ddd = int(input('Digite o DDD do celular: '))
numCelular = int(input('Digite o numero do celular: '))

print("Olá, %s"%nome)

if ddd == 49:
    print("%s VOCÊ LIGOU PARA UM TELEFONE DO VELHO OESTE"%nome)
elif ddd == 48:
    print("%s VOCÊ LIGOU PARA UM TELEFONE DO LITORAL"%nome)
elif ddd == 47:
    print("%s VOCÊ LIGOU PARA UM TELEFONE DA REGIÃO DE JOINVILLE"%nome)
else:
    print('%s VOCÊ LIGOU PARA UM TELEFONE DE FORA DE SC'%nome)
