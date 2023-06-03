n = int(input())
while n > 0:
    n -= 1
    n2 = int(input())
    entrada = list(map(int, input().split()))
    for ind, i in enumerate(entrada):
        entrada[ind] = entrada[ind]
    aux = sorted(entrada)
    aux.reverse()
    total = 0
    for ind, i in enumerate(entrada):
        if (entrada[ind] == aux[ind]):
            total +=1
    print(total)