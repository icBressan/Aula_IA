notas=[]
soma=0
media=0

while True:
    nota = int(input("Digite a nota (-1 para sair): "))

    if nota == -1:
        break
    
    notas.append(nota)
    soma += nota
    
    media = soma / len(notas)

    acima_media=0
    abaixo_seis=0
    for nota in notas:
        if nota > media:
            acima_media += 1
        if nota < 6:
            abaixo_seis += 1
    

    
    

print (f"Valores lidos: {len(notas)}")
print(f'Notas: {notas}')
print(f'Soma: {soma}')
print(f'Media: {media}')
print(f'Quantidade de valores acima da media: {acima_media}')
print(f'Quantidade de valores abaixo de 6: {abaixo_seis}')