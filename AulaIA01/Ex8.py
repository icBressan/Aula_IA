nome = input("Digite o nome completo: ")
salario_bruto = float(input("Digite o salário bruto: "))
inss = salario_bruto * 0.08
ir = salario_bruto * 0.15

print(f"Bem-vindo(a), {nome}!")
print(f"Valor do INSS: R$ {inss:.2f}")
print(f"Valor do IR: R$ {ir:.2f}")