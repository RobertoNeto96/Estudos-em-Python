valor = float(input('Digite o valor do produto: '))

desconto = 0.05
total = valor - (valor * desconto)

print(f'Seu produto no valor de R${valor:.2f} reais, com 5% de desconto fica R${total:.2f} reais')