nome = input("Digite seu nome: ")

parte_nome = ""

for i in range(1, len(nome) + 1):
    parte_nome += nome[i-1] 
    print(parte_nome)  
