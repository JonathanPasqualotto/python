import os
import time
i = 0
while True:
    os.system('clear')
    nome = str(input('Digite o nome do doador: '))
    tipo = str(input("Digite o Tipo sanguineo: "))
    if tipo == 'B-' or tipo == 'b-':
        break
    i += 1
    time.sleep(1)
print('Achou doador!')
