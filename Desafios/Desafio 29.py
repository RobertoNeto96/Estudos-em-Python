velocidade = int(input('Digite a velocidade do carro: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você estava a {velocidade}Km/h, excedendo o limite de velocidade de 80km/h. Portanto terá que pagar uma multa no valor de R${multa} Reais.')
else:
    velocidade <= 80
    print('Voce esta dentro do limite de velocidade (80Km/h)')    