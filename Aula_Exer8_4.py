viagens = 0
litros = 120.000
i = 0
while litros != 0:
    litros -= 10.000 - 10/100
    viagens += 1
    for i in range(litros > 0):
        litros -= 5.000
        viagens += 1
        i += 1
    if litros == 0.0:
        print(viagens)
        print('{:.2f}'.format(litros))
        break