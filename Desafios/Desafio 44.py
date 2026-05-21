valor = float(input('Digite o valor do produto: '))
condicao = int(input('Qual sera a forma de pagamento: \n [1] A vista [Dinheiro/Cheque] \n [2] A vista no cartão \n [3] Em ate 2x no cartão \n [4] 3x ou mais \n []'))

if condicao == 1:
    print(f'Pagando a VISTA você tem desconto de 10%. Sua compra no valor de R${valor:.2f} Reais fica com um novo valor de: R${valor - (valor * 0.10):.2f} Reais ')
elif condicao == 2:
    print(f'Pagando a VISTA no CARTÃO você tem desconto de 5%. Sua compra no valor de R${valor:.2f} Reais fica com um novo valor de: R${valor - (valor * 0.05):.2f} Reais. ')
elif condicao == 3:
    print(f'Pagando em 2x VEZES NO CARTÃO você não tem desconto algum, o valor da sua compra é R${valor:.2f} Reais')
else:
    condicao == 4
    print(f'Pagando em 3x OU MAIS NO CARTÃO a compra tem um acréscimo de 20% de juros. Sua compra no valor de R${valor:.2f} Reais fica com um novo valor de: R${valor + (valor * 0.20):.2f} Reais.')   