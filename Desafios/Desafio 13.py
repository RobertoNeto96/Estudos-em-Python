salario = float(input('Digite o salario: '))

aumento = 0.15
total = salario + (salario * aumento)

print(f'Com o aumento de 15% o salario de R${salario:.2f} reais, passa a ser R${total:.2f} reais')