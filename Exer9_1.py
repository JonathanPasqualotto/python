def EhPar(numero):
    if numero%2 == 0:
        resposta = 'S'
    else:
        resposta = 'N'
    return resposta

num = int(input("Entre com um número: "))
resultado = EhPar(num)
if resultado == 'S':
    print("O número %d é par."%num)
else:
    print("O número %d é impar."%num)
    

