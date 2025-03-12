frase = input ("Digite uma frase com espaços em branco:")

espacos = 0
vogais = 0
vogais_lista = ['a', 'e', 'i', 'o', 'u']

for letra in frase:
    if letra == ' ':
        espacos += 1
    elif letra.lower() in vogais_lista:
        vogais += 1

print(f"Quantidade de espaços em branco: {espacos}")
print(f"Quantidade de vogais: {vogais}")