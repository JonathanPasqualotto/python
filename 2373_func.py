quebrados = 0
n = 0
def verificaquebrados():
    global n, quebrados
    while n > 0:
        n -= 1
        l, c = map(int, input().split())
        if c < l:
            quebrados += c
    return print(quebrados)
        

n = int(input('entradas: '))
verificaquebrados()