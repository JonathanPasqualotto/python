def extremidades(i:int, j:int): # Verifica se o indice está em alguma das extremidades
    return i == 0 or i == largura -1 or j == 0 or j == altura-1

altura = int(input("Digite a largura do retângulo: "))
largura = int(input("Digite a altura do retângulo: "))

i = 0
while i < largura:
    j = 0
    while j < altura:
        if extremidades(i,j): # Chama a função que criamos
            print("#"  ,end = "")
        else:
            print(" ",end = "")
        j += 1
    print()
    i += 1
