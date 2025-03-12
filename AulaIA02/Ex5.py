faixa1 = 0
faixa11 = 0
faixa18 = 0

for i in range(10):
    idade = int(input("Digite a idade: "))
    if 1 <= idade <= 10:
        faixa1 += 1
    elif 11 <= idade <= 17:
        faixa11 += 1
    else:
        faixa18 += 1

print(f"Quantidade de pessoas de 1 a 10 anos: {faixa1}")
print(f"Quantidade de pessoas de 11 a 17 anos: {faixa11}")
print(f"Quantidade de pessoas com 18 anos ou mais: {faixa18}")
