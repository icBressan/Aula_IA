arquivo = open("vendas.txt", "r")

vendas = {}

primeira_linha = True

for linha in arquivo:
    if primeira_linha:
        primeira_linha = False
    else:
        linha = linha.strip()

        if linha != "":
            partes = linha.split(";")
            produto = partes[0]
            quantidade = int(partes[1])
            preco = float(partes[2])

            total = quantidade * preco

            if produto in vendas:
                vendas[produto] += total
            else:
                vendas[produto] = total

arquivo.close()

print("Total de vendas por produto:")
for produto in vendas:
    print(f"{produto}: R$ {vendas[produto]:.2f}")