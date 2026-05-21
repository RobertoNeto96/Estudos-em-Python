altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

imc = peso / (altura**2)

if imc < 18.5:
    print(f'Levando em conta seu IMC de: {imc:.2f} voce esta abaixo do peso.')
elif imc >= 18.6 and imc <= 24.9:
    print(f'Levando em conta seu IMC de: {imc:.2f} voce esta no seu peso ideal.')
elif imc >= 25 and imc <= 29.9:
    print(f'Levando em conta seu IMC de: {imc:.2f} voce esta com sobrepeso.')
elif imc >= 30 and imc <= 39.9:
    print(f'Levando em conta seu IMC de: {imc:.2f} voce esta com obesidade.')
elif imc >= 40:
    print(f'Levando em conta seu IMC de: {imc:.2f} voce esta com obesidade mórbida.')                