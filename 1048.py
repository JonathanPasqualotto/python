n = float(input())
if n >= 0 and n <= 400.00:
    rA1 = n * 0.15
    Ra1 = rA1 + n
    print("Novo salario: {:.2f}" .format(Ra1))
    print("Reajuste ganho: {:.2f}" .format(rA1))
    print("Em percentual: 15%")
elif n >= 400.01 and n <= 800.00:
    rA1 = n * 0.12
    Ra1 = rA1 + n
    print("Novo salario: {:.2f}" .format(Ra1))
    print("Reajuste ganho: {:.2f}" .format(rA1))
    print("Em percentual: 12%")
elif n >= 800.01 and n <= 1200.00:
    rA1 = n * 0.10
    Ra1 = rA1 + n
    print("Novo salario: {:.2f}" .format(Ra1))
    print("Reajuste ganho: {:.2f}" .format(rA1))
    print("Em percentual: 10%")
elif n >= 1200.01 and n <= 2000.00:
    rA1 = n * 0.07
    Ra1 = rA1 + n
    print("Novo salario: {:.2f}" .format(Ra1))
    print("Reajuste ganho: {:.2f}" .format(rA1))
    print("Em percentual: 7%")
elif n >= 2000.01:
    rA1 = n * 0.04
    Ra1 = rA1 + n
    print("Novo salario: {:.2f}" .format(Ra1))
    print("Reajuste ganho: {:.2f}" .format(rA1))
    print("Em percentual: 4%")