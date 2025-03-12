maior = 0

for i in range(10):
    idade = int(input("Digite a idade do aluno: "))
    if idade > maior:
        maior = idade

print(f"A maior idade é: {maior}")
