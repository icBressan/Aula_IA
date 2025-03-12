nome_mais_velho = ""
idade_mais_velho = 0

for i in range(10):
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    if idade > idade_mais_velho:
        idade_mais_velho = idade
        nome_mais_velho = nome

print(f"O aluno mais velho é: {nome_mais_velho}")
