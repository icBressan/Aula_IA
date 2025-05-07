from dados import nomes

nomes = nomes.replace('\n', '').split(';')

for nome in nomes:
    partes = nome.strip().split()
    if len(partes) >= 2:
        primeiro = partes[0].capitalize()
        ultimo = partes[-1].capitalize()
        print(f"{primeiro} {ultimo}")

