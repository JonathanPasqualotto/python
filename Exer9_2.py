def Antecessor(num):
    return (num - 1)

def Sucessor(num):
	return (num + 1)

num = int(input("Entre com um numero: "))
print("O sucessor do numero %d eh %d."%(num,Sucessor(num)))
print("O antesucessor do numero %d eh %d."%(num,Antecessor(num)))


