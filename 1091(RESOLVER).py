k = int(input())
#while True:
    #if k == 0:
      #  break
i = 0
while i <= k:
        N, M = int(input().split())
        X, Y = int(input().split())
        dX = X - N
        dY = Y - M
        i = i + 1

        if not dX or not dY:
            print ("divisa")
        elif dX < 0 and dY > 0:
            print ("NO")
        elif dX > 0 and dY > 0:
            print("NE")
        elif dX < 0 and dY < 0:
            print("SO")
        elif dX > 0 and dY < 0:
            print("SE")

