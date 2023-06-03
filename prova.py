def lervetor(questoes):
    for i in range(1, 11, 1):
        questoes.append(input('valor das questoes %d: '%i))

def caculadora(gabarito,questoes):
    nota = 0
    for i in range(10):
        if gabarito[i] == questoes[i]:
            nota+=1
    return nota


media = 0
alunos = 0
gabarito = []
print('entre com o abarito da prova ')
lervetor(gabarito)
while True:
    matricula = int(input('entre com o codigo do aluno: '))
    if matricula == 0:
        break
    print('entre com as respostas do aluno: ')
    respostas = []
    lervetor(respostas)
    nota = caculadora(gabarito, respostas)
    print('o aluno %d ficou com a nota = %d'%(matricula,nota))
    alunos +=1
    media += nota
print('a media da truma foi: ',media/alunos)
