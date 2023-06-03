def eastereggs(dica):
    numbers[]
    if oper == '+':
    X = numbers.pop()
    Y = numbers.pop()
    numbers.append(Y)
    numbers.append(X)
    numbers.append(X+Y)
    elif oper == '-':
        X = numbers.pop()
        Y = numbers.pop()
        numbers.append(Y)
        numbers.append(X)
        numbers.append(X-Y)
    elif oper == 'P':
        X = numbers.pop()
        numbers.pop(X)
    elif oper == 'D':
        X = numbers.ppop()
        numbers.append(X)
        numbers.append(X*2)
        else:
            numbers.append(int(oper))
            return numbers


print('if you have watched player number one, do you know an easter egg is...')
print('Para comemorar o retorno das aulas...')
print('temos F - 53 + 50 - A + 48 - 49 add easter eggs disponiveis...')
print('quem vai conseguir encontra-los')
print('the first input hides the room(s) where the easter eggs will be...')
entrada = ['1', '65', '1', 'P', '66', '2', '0', '1', 'D', '+', '1',
           '+', 'P', '66', '-', '1', '2', '0', '5', 'D', '9', '4', 'P']
saida = eastereggs(entrada)
