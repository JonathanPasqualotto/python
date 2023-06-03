def Divisores(num):
    nDivisor = 2
    for i in range(2,num,1):
        if num % i == 0:
            nDivisor +=1
    return nDivisor

num = int(input("Entre com um numero: "))
print("O número %d tem %d divisores."%(num,Divisores(num)))


