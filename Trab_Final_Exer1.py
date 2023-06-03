def mergeSort(lista):

    if len(lista) > 1:
        meio = len(lista)//2
        listaDaEsquerda = lista[:meio]
        listaDaDireita = lista[meio:]
        mergeSort(listaDaEsquerda)
        mergeSort(listaDaDireita)
        i = 0
        j = 0
        k = 0
        while i < len(listaDaEsquerda) and j < len(listaDaDireita):
            if listaDaEsquerda[i] < listaDaDireita[j]:
                lista[k]=listaDaEsquerda[i]
                i += 1
            else:
                lista[k]=listaDaDireita[j]
                j += 1
            k += 1
        while i < len(listaDaEsquerda):

            lista[k]=listaDaEsquerda[i]
            i += 1
            k += 1
        while j < len(listaDaDireita):
            lista[k]=listaDaDireita[j]
            j += 1
            k += 1
    return lista

casos = int(input())
while casos > 0:
    casos -= 1
    cont = 0
    
    n = int(input())
    arr = list(map(int, input().split()))
    aux = arr.copy()
    retorno = mergeSort(arr)
    invert = retorno[::-1]
    for i in range(n):
        if aux[i] == invert[i]:
            cont += 1
    print(cont)