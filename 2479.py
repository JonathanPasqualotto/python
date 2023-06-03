import os
os.system('clear')

lista_nomes = []
bom = 0
entrada = int(input())
for i in range(entrada):
    sinal, nome = input().split()
    lista_nomes.append(nome)
    if sinal == '+':
        bom += 1


lista_nomes.sort()
for i in lista_nomes:
    print(i)

print('Se comportaram: %d | Nao se comportaram: %d' % (bom, len(lista_nomes) - bom))
