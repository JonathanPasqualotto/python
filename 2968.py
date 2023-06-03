import math
import os

os.system('clear')

valores = list(map(int,input().split()))
total_placas = valores[0] * valores[1]

result = []

for i in range(1,10):
    perc = i /10
    qtd_placas = total_placas * perc
    qtd_tot = str(math.ceil(qtd_placas))
    result.append(qtd_tot)

result_fim = " ".join(result)
print(result_fim)