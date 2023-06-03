n = int(input())
ant = n % 10
n = n // 10;
iguais = False;
pos = 0
while n > 0 and not iguais:
    at = n % 10
    if at == ant:
        iguais = True
    else:
        pos += 1
    ant = at
    n = n // 10
if iguais:
    print("sim")
else:
    print("não")
