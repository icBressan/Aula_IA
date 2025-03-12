intervalo = 0
soma = 0

for i in range(10):
    num = int(input("Digite um número: "))
    if 70 <= num <= 90:
        intervalo += 1
        soma += num

if intervalo > 0:
    media = soma / intervalo
    print(f"Quantidade de números no intervalo de 70 a 90: {intervalo}")
    print(f"Soma dos números no intervalo de 70 a 90: {soma}")
    print(f"Média dos números no intervalo de 70 a 90: {media}")
else:
    print("Nenhum número no intervalo de 70 a 90.")
