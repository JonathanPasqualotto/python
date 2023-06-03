n = int(input())
f = 0
q = 0
while n>0:
    q = n%10
    n = (n-q)//10
    f += q
print(f) 