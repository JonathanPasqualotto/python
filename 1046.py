h = input().split()
a, b = h
a = int(h[0])
b = int(h[1])
if a < b:
    temp = b - a
else:
    temp = (24 - a) + b
print("O JOGO DUROU {} HORA(S)".format(temp))