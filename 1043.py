#| b - c | < a < b + c
#| a - c | < b < a + c
#| a - b | < c < a + b

#|10 – 9| < 5 < 10 + 9
#1 < 5 <19 (VERDADEIRO)

#|9 – 5| < 10 < 9 + 5
#4 < 10 < 14 (VERDADEIRO)

#|5 – 10| < 9 < 10 + 5
#5 < 9 < 15 (VERDADEIRO)

a, b, c  = map(float, input().split())
if abs(b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print('Perimetro = {:.1f}'.format(a + b + c))
else:
    print('Area = {:.1f}'.format(((a + b) / 2) * c))

