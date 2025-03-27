def carregaAlunosNotas():
    alunos =[]
    notas =[]

    for i in range(5):
        nome= input('Digite o nome do aluno: ')
        nota= float(input('Digite a nota do aluno: '))
        print()

        alunos.append(nome)
        notas.append(nota)
    
    print(f'Alunos: {alunos}')
    print(f'Notas: {notas}')

print('Exemplo 2')
carregaAlunosNotas()