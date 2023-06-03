import ctypes
while True:
    try:
        n1, n2 = map(int, input().split())
        ctypes.c_ulong(-1)
        print(n1^n2)
    except EOFError:
        break