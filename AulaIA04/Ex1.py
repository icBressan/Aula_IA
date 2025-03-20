string = input().upper()

if string not in ['A','T','C','G']:
    print('String inválida')
else:
    if string == 'A':
        print('T')  
    elif string == 'T':
        print('A') 
    elif string == 'C':
        print('G') 
    elif string == 'G':
        print('C')  