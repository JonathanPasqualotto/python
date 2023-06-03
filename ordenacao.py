from cmath import pi


x = int(input())
y = int(input())
z = int(input())

if x < y and x < z and y < z:
    print("crescente")
else:
    print("não está em ordem crescente")
