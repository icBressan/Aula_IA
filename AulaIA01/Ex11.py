aulas_semanais = int(input("Digite a quantidade de aulas semanais: "))
valor_hora_aula = float(input("Digite o valor da hora/aula: "))

salario_bruto = aulas_semanais * valor_hora_aula * 4
segundo_bruto = salario_bruto * 6.2
inss = segundo_bruto * 0.115
ir = (segundo_bruto - inss) * 0.175

print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"Segundo cálculo bruto: R$ {segundo_bruto:.2f}")
print(f"Desconto INSS: R$ {inss:.2f}")
print(f"Desconto IR: R$ {ir:.2f}")