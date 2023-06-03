num = int(input())

for i in range(0,num):
    num2 = int(input())
    j = 1
    k = 0
    while j <= num2:
        if num2 % j == 0:
            k += 1
        j += 1
    if k > 2:
        print('{} nao eh primo'.format(num2))
    else:
        print('{} eh primo'.format(num2))
