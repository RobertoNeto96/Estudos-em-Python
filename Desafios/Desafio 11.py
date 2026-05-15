import math

largura = float(input('Digite a LARGURA da parede: '))
altura = float(input('Digite a ALTURA da parede:'))

area = largura * altura
tinta = 2

print(f'Para pintar a parede com {area}m² voce irá precisar de {math.ceil(area / tinta)} latas de tinta')