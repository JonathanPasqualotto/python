#cria uma condição verdadeira
while True:
    n = int(input())       #recebe um valor inteiro
    if n == 0:              #esse valor não pode ser zero se for o programa encerra
        break
    h = [int(x) for x in input().split()]   #recebe todos os valores possiveis, criando uma lista denominada "h"
    h.append(h[0])          #adiciona o valor recebi no inicio da lista primeiro posição
    h.append(h[1])          #adiciona o valor recebi no inicio da lista segunda posição
    picos = 0
    for i in range(1, n+1):           #sequecia criada a partir do valor recebido por "n+1" do primeiro inputt
    
    #verifica de "i" é menor que o antecessor ou menor que o sucessor
    #se positivo acumula o valor na variavel picos
        if h[i] < h[i-1] and h[i] < h[i+1]:     
            picos += 1

    #verifica de "i" é maior que o antecessor ou maior que o sucessor
    #se positivo acumula o valor na variavel picos
        elif h[i] > h[i-1] and h[i] > h[i+1]:
            picos += 1
    print(picos)
