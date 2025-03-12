maior = 0
menor = 0

for i in range(10):
    num = int(input("Digite um número: "))
    if num >= 10:
        maior += 1
    else:
        menor += 1

print(f"Quantidade de números maior ou igual a 10: {maior}")
print(f"Quantidade de números menor que 10: {menor}")
