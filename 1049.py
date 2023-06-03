a, b, c = input().split()

if a == 'vertebrado' and b == 'ave' and c == 'carnivoro':
    x = 'aguia'

elif a == 'vertebrado' and b == 'ave' and c == 'onivoro':
    x = 'pomba'

elif a == 'vertebrado' and b == 'mamifero' and c == 'onivoro':
    x = 'homem'

elif a == 'vertebrado' and b == 'mamifero' and c == 'herbivoro':
    x = 'vaca'

elif a == 'invertebrado' and b == 'inseto' and c == 'hematofago':
    x = 'pulga'

elif a == 'invertebrado' and b == 'inseto' and c == 'herbivoro':
    x = 'lagarta'

elif a == 'invertebrado' and b == 'anelideo' and c == 'hematofago':
    x = 'sanguessuga'

elif a == 'invertebrado' and b == 'anelideo' and c == 'onivoro':
    x = 'minhoca'
print(x)