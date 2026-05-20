valor_casa = float(input('Digite o valor da casa: '))
parcelas = int(input('Em quantas vezes deseja pagar? '))
salario = float(input('Digite o seu salario: '))

valor_parcelas = valor_casa / parcelas   
porcentagem_salario = salario * 0.30

if valor_parcelas < porcentagem_salario:
    print(f'Emprestimo \033[1;32mAPROVADO\033[m \n Você pagará R${valor_casa:.2f} em {parcelas} vezes \n Valor da parcela R${valor_parcelas:.2f} Reais')
elif valor_parcelas > porcentagem_salario:
    print(f'Emprestimo \033[1;31mNEGADO\033[m \n Valor da parcela excede o limite de 30% do seu salario \n Valor da parcela R${valor_parcelas:.2f} Reais \n 30% do salario R${porcentagem_salario:.2f} Reais')    