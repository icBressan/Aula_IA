maior = 0
menor = 100 

for i in range(10):
    idade = int(input("Digite a idade do aluno: "))
    if idade > maior:
        maior = idade
    if idade < menor:
        menor = idade

media = (maior + menor) / 2
print(f"A maior idade é: {maior}")
print(f"A menor idade é: {menor}")
print(f"A média entre a maior e a menor idade é: {media}")

