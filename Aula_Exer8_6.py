i = 0
j = 0
k = 0

for volta in range(1, 11):
    print('Volta numero', volta)

    if volta % 2 == 0:
        for abdominal in range(1, 51):
            print(abdominal, 'abdominal')
            abdominal += 1
        volta += 1
        for flexao in range(1, 11):
            print('Flexão', flexao)
            flexao += 1
