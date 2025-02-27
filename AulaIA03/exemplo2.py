print ("Exemplo 2")

nome = "Isabelle"
idade = 19

print ("Olá", nome, "voce tem a idade de", idade)

frase= "ola " + nome + " voce tem a idade de " +str(idade)
print(frase)

frase = "Olá {} voce tem a idade de {}"
print(frase.format(nome,idade))

frase = f"olá {nome}, voce tem a idade de {idade}"
print(frase)

salario = 1500
frase = f"salario é {salario:.2f}"
print(frase)