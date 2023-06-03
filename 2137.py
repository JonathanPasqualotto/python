
def ordena(n):
    lista = []
    for i in range(n):
        lista.append(input())
    lista.sort()
    return lista

        

while True:
    try:
        entrada = int(input())
        res = ordena(entrada)
        for i in res:
            print(i)
    except EOFError:
        break
    
