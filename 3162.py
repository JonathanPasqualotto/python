import math
cases = int(input())
naves = []
for a in range(cases):
    coordenadas = list(map(int,input().split()))
    naves.append(coordenadas)
for nave in naves:
    distancias = []
    for outras in naves:
        if outras == nave:
            continue
        distancia = math.sqrt((outras[0] - nave[0])**2 + (outras[1]-nave[1])**2 + (outras[2]-nave[2])**2)
        distancias.append(distancia)
    menor = min(distancias)
    if menor <=20.0:
        print("A")
    elif menor > 20.0 and menor <=50.0:
        print('M')
    else:
        print('B')