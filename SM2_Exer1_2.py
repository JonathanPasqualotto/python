def Menu():
    x = int(input('Digite um valor para saber se é primo: '))
    primo(x)
    print(primo(x))


def primo(val):
    if val % 3 == 0:
        return 'É primo'
    else:
       return 'Não é primo'

Menu()