from dados import nomes, faltas

nomes = nomes.replace('\n', '').split(';')

faltas_temp = faltas.split(';')
faltas = []
for falta in faltas_temp:
    faltas.append(int(falta))

reprovados = []
for i in range(len(faltas)):
    if faltas[i] > 20:
        reprovados.append(nomes[i])

print("Alunos reprovados por falta:")
for nome in reprovados:
    print(nome)
print(f"Total de reprovados por falta: {len(reprovados)}")

