while True:
    entrada = int(input())
    if entrada == 0 :
        break
    inicial = []
    for i in range(1,entrada+1):
        inicial.append(i)
    resultado = []
    while len(inicial) > 1:
        resultado.append(inicial.pop(0))
        inicial.insert(len(inicial)-1,inicial.pop(0))
    print("Discarded cards: " + str(resultado).replace("[","").replace("]",""))
    print("Remaining card: " + str(inicial[0]))