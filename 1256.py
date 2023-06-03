n = int(input())
for i in range(n):
    hash = {}
    m,c = map(int,input().split())
    for h in range(m):
        hash[h] = []
    num = list(map(int,input().split()))
    for j in num:
        r = j%m
        hash[r].append(j)
    for k in range(m):
        print('%d -> '%k,end='')
        for t in (hash[k]):
            print('%d -> '%t,end='')
        print('\\',end='')
        print()
    if i < n-1:
        print('')