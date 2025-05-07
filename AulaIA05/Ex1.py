from dados import nomes, notas, faltas

nomes = nomes.replace('\n', '').split(';')

notas_str = notas.split(';')
notas = []
for nota in notas_str:
    notas.append(float(nota))

faltas_str = faltas.split(';')
faltas = []
for falta in faltas_str:
    faltas.append(int(falta))

print(f"Total de nomes: {len(nomes)}")
print(f"Total de notas: {len(notas)}")
print(f"Total de faltas: {len(faltas)}")