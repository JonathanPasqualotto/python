import os
os.system('clear')
import heapq
n = int(input())

min = 1<<64
stack = []
queue = []
values = {}

for i in range(n):
    opcao = input()

    if len(opcao) > 3:
        a, b = opcao.split()
        b = int(b)
        stack.append(b)
        heapq.heappush(queue, b)

        if b in values:
            values[b] += 1
        else:
            values[b] = 0
    elif opcao == 'POP':
        if len(stack) > 0:
            numero = stack.pop()
            values[numero] -= 1
        else:
            print('EMPTY')
    elif opcao == 'MIN':
        if len(stack) > 0:  
            while queue:
                numero = heapq.heappop(queue)
                if values[numero] >= 0:
                    print(numero)
                    heapq.heappush(queue, numero)
                    break
        else:
            print('EMPTY')