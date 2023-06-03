def contagem(n):
    dif = 0
    for i in range(n):
        x = int(input())
        if x != 1:
            dif += 1
    return print(dif)

n = int(input())
contagem(n)