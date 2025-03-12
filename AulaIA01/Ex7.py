quantidade = int(input("Digite a quantidade do produto: "))
preco = float(input("Digite o preço do produto: "))

subtotal = quantidade * preco
desconto = subtotal * 0.17
total = subtotal - desconto

print(f"Subtotal: R$ {subtotal:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Total a pagar: R$ {total:.2f}")