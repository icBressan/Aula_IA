string1 = input("String 1:")
string2 = input("String 2:")

print("Tamanho de", string1, ":",len(string1),"caracteres")
print("Tamanho de", string2, ":",len(string2),"carateres")

if len(string1) == len(string2):
    print("As strings possuem o mesmo tamanho.")
else:
    print("As strings são de tamanho diferentes")

if string1 == string2:
    print("As strings são iguais.")
else:
    print("As strings são diferentes.")