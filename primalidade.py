n = int(input())
primo = True
divisor = 2
while divisor < n and primo: # equivalente a "div... and é_primo == True:"
    if n % divisor == 0:
        primo = False
    divisor += 1
if primo and n != 1:
    print("primo")
else:
    print("não primo")