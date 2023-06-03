'''Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros, verifica se tal lista possui elementos repetidos e os remove.
A função deve devolver uma lista correspondente à primeira lista, sem elementos repetidos. 
A lista devolvida deve estar ordenada.'''
def remove_repetidos(lista):
    li = []
    for i in lista:
        if i not in li:
            li.append(i)
    li.sort()
    return li

lista = [1, 1, 2, 1, 3, 4, 3, 6, 7, 6, 7, 8, 10 ,9]

lista = remove_repetidos(lista)
print (lista)
