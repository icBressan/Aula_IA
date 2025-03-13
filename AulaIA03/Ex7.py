telefone = input("Digite o número de telefone com DDD (apenas números): ")

numero_valido = True
for caracter in telefone:
    if caracter < '0' or caracter > '9':  
        numero_valido = False
        break

if len(telefone) == 11 and numero_valido:
    ddd_primeiro_caracter = telefone[0]
    ddd_segundo_caracter = telefone[1]
    ddd = ddd_primeiro_caracter + ddd_segundo_caracter  

    numero_primeiro_caracter = telefone[2]
    numero_2 = telefone[3]
    numero_3 = telefone[4]
    numero_4 = telefone[5]
    numero_5 = telefone[6]
    numero_6 = telefone[7]
    numero_7 = telefone[8]
    numero_8 = telefone[9]
    numero_9 = telefone[10]

    numero_formatado = f"({ddd}) {numero_primeiro_caracter}{numero_2}{numero_3}{numero_4}{numero_5}-{numero_6}{numero_7}{numero_8}{numero_9}"

    print(f"Número formatado: {numero_formatado}")
else:
    print("Número inválido! O telefone deve ter 11 dígitos numéricos.")
