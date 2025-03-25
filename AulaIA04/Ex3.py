x = []
y = []

print("Digite 5 elementos para o vetor X:")
for i in range(5):
    x.append(int(input()))

print("Digite 5 elementos para o vetor Y:")
for i in range(5):
    y.append(int(input()))

soma = []
for i in range(5):
    soma.append(x[i] + y[i])

produto = []
for i in range(5):
    produto.append(x[i] * y[i])

diferenca = []
for elemento in x:
    if elemento not in y:
        diferenca.append(elemento)

intersecao = []
for elemento in x:
    if elemento in y and elemento not in intersecao:
        intersecao.append(elemento)

uniao = x[:]  
for elemento in y:
    if elemento not in uniao:
        uniao.append(elemento)

print("Soma entre X e Y:", soma)
print("Produto entre X e Y:", produto)
print("Diferença entre X e Y:", diferenca)
print("Interseção entre X e Y:", intersecao)
print("União entre X e Y:", uniao)