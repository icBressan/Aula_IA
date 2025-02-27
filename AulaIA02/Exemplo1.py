nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
frequencia = float(input("Digite a frequência: "))

media = (nota1+nota2)/2
print("A média é",media)

if media >= 6 and frequencia >= 75:
    print("O aluno está aprovado!")
    print("Já pode curtir as férias 😎")
elif media >= 2:
    print("O aluno está de exame!")
    print("Precisa estudar mais um pouco...")
else:
    print("O aluno está reprovado!")
    print("Não há direito a exame.")