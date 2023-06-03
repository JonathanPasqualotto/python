n = int(input())
n1 = list(map(int, input().split()))
s = 0
for num in n1:
    s += num
print(s)