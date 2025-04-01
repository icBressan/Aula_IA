def carregaAlunosNotas():
    alunos = []
    notas = []

    for i in range(5):
        nome = input('Digite o nome do aluno: ')
        nota = float(input('Digite a nota do aluno: '))
        print()

        alunos.append(nome)
        notas.append(nota)

    return [alunos, notas]

def nomeAlunoMaiorNota(matriz):
    alunos = matriz[0]
    notas = matriz[1]

    maior_nota = notas[0]  # Assume que a primeira nota é a maior
    aluno_maior = alunos[0]  # Assume que o primeiro aluno tem a maior nota

    for i in range(1, len(notas)):
        if notas[i] > maior_nota:
            maior_nota = notas[i]
            aluno_maior = alunos[i]

    return aluno_maior, maior_nota  

print('Exemplo 2')
dados = carregaAlunosNotas()
aluno, nota = nomeAlunoMaiorNota(dados)

print(f'O aluno com a maior nota é {aluno}. Nota: {nota:.2f}.')
