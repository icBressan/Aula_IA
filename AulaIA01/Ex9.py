valor_prestacao = float(input("Digite o valor da prestação: "))
taxa_juros = float(input("Digite a taxa de juros (%): "))
tempo_atraso = int(input("Digite o tempo de atraso (dias): "))

prestacao = valor_prestacao + (valor_prestacao * (taxa_juros / 100) * tempo_atraso)
print(f"Valor da prestação em atraso: R$ {prestacao:.2f}")
