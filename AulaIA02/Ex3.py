intervalo = 0

for i in range(10):
    num = int(input("Digite um número: "))
    if 10 <= num <= 20:
        intervalo += 1

print(f"Quantidade de números no intervalo de 10 a 20: {intervalo}")
