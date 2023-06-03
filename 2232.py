t = int(input())
vet = []

for i in range(0,t,1):
    vet.append(int(input()))

for i in vet:
    print(2**i-1)