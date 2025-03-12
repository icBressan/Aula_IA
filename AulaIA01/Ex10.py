tempo_viagem = float(input("Digite o tempo gasto na viagem (horas): "))
velocidade_media = float(input("Digite a velocidade média (km/h): "))
distancia = tempo_viagem * velocidade_media
consumo = distancia / 12

print(f"Distância percorrida: {distancia:.2f} km")
print(f"Quantidade de combustível utilizada: {consumo:.2f} litros")