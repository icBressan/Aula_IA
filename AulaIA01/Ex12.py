limite_utilizado = float(input("Digite o valor do limite utilizado: "))
dias_utilizados = int(input("Digite a quantidade de dias de uso: "))
taxa_juros_mensal = float(input("Digite a taxa de juros mensal (%): "))

taxa_diaria = taxa_juros_mensal / 30
juros = (limite_utilizado * (taxa_diaria / 100)) * dias_utilizados

print(f"Valor dos juros: R$ {juros:.2f}")