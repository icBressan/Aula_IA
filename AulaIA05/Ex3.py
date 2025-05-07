from dados import nomes, notas

nomes = nomes.replace('\n', '').split(';')

notas_temp = notas.split(';')
notas = []
for nota in notas_temp:
    notas.append(float(nota))

aprovados = []
for i in range(len(notas)):
    if notas[i] >= 6.0:
        aprovados.append(nomes[i])

print("Alunos aprovados:")
for nome in aprovados:
    print(nome)
print(f"Total de aprovados: {len(aprovados)}")
