import os

os.system('clear')


contagem = 0
def valorTeste(voltas):
    global contagem
    for i in range(teste):
        if voltas[i] % 2 == 1:
            contagem -= 1
        else:
            for i in range(teste):
                if voltas[i] % 2 == 0:
                    contagem += 1
    return contagem


voltas = []
pessoas = []
teste = int(input())
for i in range(teste):
    nome,valor = input().split()
    valor = int(valor)
    pessoas.append(nome)
    voltas.append(valor)
    if nome == 0 and valor == 0:
        break
#print(pessoas)
valorTeste(voltas)

if contagem < 0:
    for contagem in pessoas:
        print(contagem)

#print(contagem)
#print(voltas)
#print(cont)
