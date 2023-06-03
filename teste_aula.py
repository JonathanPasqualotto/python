def fatorial(n):
    n = int(input())
    fat = 1
    while (n > 1):
        fat = fat * n
        n = n - 1
    return fat

def numero_binomial(n, k):
    return fatorial(n) / (fatorial(k) * fatorial(n-k))

def testa_fatorial():
    if fatorial(1) == 1:
        print("ok")
    else:
        print("nao 1")
    if fatorial(2) == 2:
        print("ok")
    else:
        print("nao 2")
    if fatorial(0) == 1:
        print("ok")
    else:
        print("nao 0")
    if fatorial(5) == 120:
        print("ok")
    else:
        print("nao 5")
