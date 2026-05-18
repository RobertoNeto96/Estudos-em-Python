km = float(input('Qantos Km da sua viagem? '))

if km <= 200:
    print(f'Viagens abaixo de 200Km de distancia, custam R$0.50 centavos por Km, sendo assim sua passagem ficou no valor de R${km * 0.50:.2f} Reais.')
else:
    print(f'Viagens acima de 200Km de distancia, custam R$0.45 centavos por Km, sendo assim, sua passagem ficou no valor de R${km * 0.45:.2f} Reais')    