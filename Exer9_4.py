def Fatorial(num):
    Fat = 1
    for i in range(1,num+1,1):
        Fat *= i
    return Fat
    
def FatorialRecursivo(num):
    if num <= 1:
        return 1
    else:
        return num * FatorialRecursivo(num-1)
    

num = int(input("Entre com um numero: "))
print("O fatorial de %d = %f."%(num,Fatorial(num)))
print("O fatorial recursivo de %d = %f."%(num,FatorialRecursivo(num)))


