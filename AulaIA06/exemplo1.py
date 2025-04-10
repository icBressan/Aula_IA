arquivo = open('aula.txt','w')

nome = input('Digite o nome do aluno: ')
arquivo.write(nome + '\n')

nota1 = input('Digite a nota 1: ')
arquivo.write(nota1 + '\n')

nota2 = input('Digite a nota 2: ')
arquivo.write(nota2 + '\n')

arquivo.close()

print('Arquivo gerado com sucesso!')