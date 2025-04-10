arquivo = open('aula.txt','r')
linhas = arquivo.readlines()
arquivo.close()

print(linhas)
print('Tamanho do vetor: ', len(linhas))

for linha in linhas:
    print (linha.strip())