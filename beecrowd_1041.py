#Leia 2 valores com uma casa decimal (x e y), que devem representar as coordenadas de um ponto em um plano. 
#A seguir, determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).
#Se o ponto estiver na origem, escreva a mensagem “Origem”.
#Se o ponto estiver sobre um dos eixos escreva “Eixo X” ou “Eixo Y”, conforme for a situação.

#entrada com as coordenadas
p = input().split()

#recebe o valor das entradas e adiciona eles nas variaveis x,y pela ordem digitada
x,y = p

#como voce recebe valores em string precisa ser "transformado" em flutuante
x = float(x)
y = float(y)

#primeira condiçao do eixo y
if x == 0:
    if y == 0:
        print("Origem")
    if y != 0:
        print("Eixo Y")

#segunda condição do eixo x
if y == 0:
    if x != 0:
        print("Eixo X")

#condição para  Q1 e Q4
if x > 0:
    if y > 0:
        print("Q1")
    if y < 0:
        print("Q4")

#condição para Q2 e Q3
if x < 0:
    if y > 0:
        print("Q2")
    if y < 0:
        print("Q3")