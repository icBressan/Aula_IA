nome = input("Digite seu nome (letras maiusculas ou minusculas): ")
contrario = ""

for i in nome.upper():
    contrario = i + contrario
    
print(contrario)