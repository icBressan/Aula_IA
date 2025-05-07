from dados import nomes

nomes = nomes.replace('\n', '').split(';')

for nome in nomes:
    partes = nome.strip().split()
    if len(partes) >= 2:
        resultado =  partes[0].capitalize() + " "
        for parte in partes[1:-1]:
            resultado += parte[0].upper() + ". "
        resultado += partes[-1].capitalize()
        print(resultado)
