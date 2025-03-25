string = input().upper()
dna = ""

for letra in string:
        if letra not in ['A','T','C','G']:
            print('String inválida')
        elif letra == 'A':
            dna += 'T' 
        elif letra == 'T':
            dna += 'A'
        elif letra == 'C':
            dna += 'G'
        elif letra == 'G':
            dna += 'C'
        

print(dna)