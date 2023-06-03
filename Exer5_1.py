n = int(input('Digite um número qualquer sem pontou e sem vírgula: '))

if n == 0:
    print ("Número é neutro")
elif (n % 2) == 0:
    print ('Número é par')
else:
    print ('Número é ímpar')