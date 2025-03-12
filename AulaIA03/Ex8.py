nome_completo = input("Digite seu nome completo: ")

abreviado = ""
parte_atual = ""

for i in range(len(nome_completo)):
    if nome_completo[i] != ' ': 
        parte_atual += nome_completo[i]
    else:
        if abreviado == "":  
            abreviado += parte_atual
        else:
            abreviado += " " + parte_atual[0] + "."  
        parte_atual = "" 

abreviado += " " + parte_atual

print(f"Nome abreviado: {abreviado}")
