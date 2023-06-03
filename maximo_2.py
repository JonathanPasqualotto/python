def maximo(x,y):
    if y > x:
        max = y
    if y < x:
        max = x
    if x > y:
        max = x
    if x < y:
        max = y

    return max
