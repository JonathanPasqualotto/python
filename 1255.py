test = int(input())

for i in range(test):
    pal = input().lower()
    carac = {}
    for c in pal:
        if c.isalpha() and c not in carac:
            carac[c] = pal.count(c)

    carac_ord = sorted(carac.items(), key=lambda x: (-x[1],x[0]))
    maior = carac_ord[0][1]
    result = ''
    for c in carac_ord:
        if c[1] == maior:
            result += c[0]
        else:
            break
    print(result)