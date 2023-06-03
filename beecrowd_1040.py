#Leia quatro números (N1, N2, N3, N4), cada um deles com uma casa decimal, correspondente às quatro notas de um aluno. 

# 1 - Calcule a média com pesos 2, 3, 4 e 1, respectivamente, para cada uma destas notas e mostre esta média acompanhada pela mensagem "Media: ". 
# 2 - Se esta média for maior ou igual a 7.0, imprima a mensagem "Aluno aprovado.".
# 3- Se a média calculada for inferior a 5.0, imprima a mensagem "Aluno reprovado.". 
# Se a média calculada for um valor entre 5.0 e 6.9, inclusive estas, o programa deve imprimir a mensagem "Aluno em exame.".

#No caso do aluno estar em exame,
# 1- leia um valor correspondente à nota do exame obtida pelo aluno. Imprima então a mensagem "Nota do exame: " acompanhada pela nota digitada. 
# 2- Recalcule a média(some a pontuação do exame com a média anteriormente calculada e divida por 2). 
# 3- imprima a mensagem "Aluno aprovado." (caso a média final seja 5.0 ou mais ) ou "Aluno reprovado.", (caso a média 
# tenha ficado 4.9 ou menos). Para estes dois casos (aprovado ou reprovado após ter pego exame) 
# 4- apresente na última linha uma mensagem "Media final: " seguido da média final para esse aluno.
#PARA POSTAR NO BEECROWD É PRECISO TROCAR AS VARIASVEIS QUE TEM NOME POR UMA LETRA SIMPLES..

#ler os 4 numeros
n = input().split()

#acrescentar os numeros em variaveis distintas.
a,b,c,d = n

#1 - sera preciso transformar os valores em flutuantes por causa das casas decimais.. por isso o comando float
#para calcular o peso de um nota multiplicasse o valor da variavel pelo peso corespondente exemplo
#variavel a*2 ao final somam-se todos os valores obtidos e divide pela media base que obtemos somando os valores dos pesos
#nesse caso é 10..
media = (float(a) * 2 + float(b) * 3 + float(c) * 4 + float(d) * 1) / 10
print("Media: {:.1f}".format(media))                    #print o resultado anterior com uma casa depois da virgula
if media >= 7.0:                                        #comparação se for maior ou igual a 7..
    print("Aluno aprovado.")
if media <= 5.0:                                        #comparação se for menor ou igual a 5
    print("Aluno reprovado.")

#a variavel media fica entre as comparações pois se 5.0 é menor ou igual a ela OU se ela for menor ou igual a 6.9 daa-se a sequencia  
if 5.0 <= media <= 6.9:
    print("Aluno em exame.")
    e =  float(input())                                        #pede a nota do exame para o usuario..
    print("Nota do exame: {:.1f}".format(e))
    nota = (media + e) / 2                                     #faz o calcula da media novamente somando a media anterior a nova e divide por 2..
    if nota >=5:                                               #comparação se for maior ou igual a 5
        print("Aluno aprovado.")
        print("Media final: {:.1f}".format(nota))
    else:                                               #comparação se for menor ou igual a 5
     print("Aluno reprovado.")
     print("Media final: {:.1f}".format(nota))
    
    


