import math

def delta(a, b, c):
    return b ** 2 - 4 * a * c

def main():
    a = float(input("valor a: "))
    b = float(input("valor b: "))
    c = float(input("valor c: "))
    imprime_raizes(a, b, c)

def imprime_raizes(a, b, c):
    d = delta(a, b, c)
    if d == 0:
        raiz1 = (-b + math.sqrt(d)) / (2 * a )
        print("a unica raiz é: ", raiz1)
    else:
        if d < 0:
            print("esta equação nao possui raiz real")
        else:
            raiz1 = (-b + math.sqrt(d)) / (2 * a)
            raiz2 = (-b - math.sqrt(d)) / (2 * a)
            print("raiz 1: ", raiz1)
            print("raiz 2: ", raiz2)
