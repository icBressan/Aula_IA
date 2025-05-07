from dados import nomes, notas, faltas

nomes = nomes.replace('\n', '').split(';')

notas_temp = notas.split(';')
notas = []
for nota in notas_temp:
    notas.append(float(nota))

faltas_temp = faltas.split(';')
faltas = []
for falta in faltas_temp:
    faltas.append(int(falta))

for i in range(len(nomes)):
    print("Nome:", nomes[i])
    print("Nota:", notas[i])
    print("Falta:", faltas[i])
    print()