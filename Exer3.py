p1 = float(input('Digite a nota da primeira prova: \n'))
p2 = float(input('Digite a nota da segunda prova: \n'))
p3 = float(input('Digite a nota da terceira prova: \n'))
t1 = float(input('Digite a nota do trabalho: \n'))
abono = float(input('Digite o valor do abono: \n'))

a1 = (p1 + p2 + p3 +(t1 + abono))/4

if a1 >= 7.0:
    print("APROVADO.")
if a1 >=4.0 and a1 <=6.9:
    print("PRESTAR A2.")
if a1 < 4.0:
    print("REPROVADO DIRETO.")