from dados import nomes

nomes = nomes.replace('\n', '').split(';')

silva = []
for nome in nomes:
    if 'SILVA' in nome.split():
        silva.append(nome)

print("Alunos com sobrenome 'SILVA':")
for nome in silva:
    print(nome)
print(f"Total com sobrenome SILVA: {len(silva)}")
