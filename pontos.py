import math
x1 = float(input())
x2 = float(input())
y1 = float(input())
y2 = float(input())

dis = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
if dis >= 10.0:
    print("longe")
else: 
    dis <= 9.9
    print("perto")
