alunos = int(input('Quantos alunos tem na turma de Algoritimos: '))
i = 0
somanot = 0
for i in range(1,alunos+1,1):
    nota = float(input('Informe a nota do aluno %d: '%i))
    somanot = somanot + nota
    i += 1
media = somanot / alunos
print('A soma total das notas é: %d'%media)