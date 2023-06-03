a,b,c = map(int,input().split())

if a != b + c and b != a + c and c != a + b and a != b and a != c and b != c:
    print("N")
else:
    print("S")