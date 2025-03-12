votos_10 = 0
votos_35 = 0
votos_nulos = 0

for i in range(10):
    voto = int(input("Digite seu voto (10 para Monteiro Lobato, 35 para Euclides da Cunha): "))
    if voto == 10:
        votos_10 += 1
    elif voto == 35:
        votos_35 += 1
    else:
        votos_nulos += 1

if votos_10 > votos_35:
    vencedor = "Monteiro Lobato"
else:
    vencedor = "Euclides da Cunha"

print(f"Quantidade de votos para Monteiro Lobato: {votos_10}")
print(f"Quantidade de votos para Euclides da Cunha: {votos_35}")
print(f"Quantidade de votos nulos: {votos_nulos}")
print(f"O vencedor é: {vencedor}")
