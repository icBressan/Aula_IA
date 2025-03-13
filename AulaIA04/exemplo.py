alunos = ['Felipe','Isabelle','Pedro','Ligia','Mateus']

print(alunos)
print(f'O primeiro aluno no vetor é {alunos[0]}')
print(f'O último aluno no vetor é {alunos[4]}')
print(f'O valor {alunos[-5]}')
print(f'O valor {alunos[-1]}')

print()
print('FOR:')
for nome in alunos:
    print(nome)

print()
print('FOR POSIÇÃO:')
for i in range(5):
    print(f'Na posicao {i} temos o valor {alunos[i]}')