def retornaConceito(nota):
    if nota >= 0.0 and nota < 5.0:
        return 'D'
    elif nota < 7.0:
        return 'C'
    elif nota < 9.0:
        return 'B'
    else:
        return 'A'


nota = float(input('Entre com a nota: '))
conceito = retornaConceito(nota)
print('A nota %0.2f tem conceito %c'%(nota,conceito))