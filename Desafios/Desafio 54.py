from datetime import date

ano_atual = date.today().year

maior = 0
menor = 0

for c in range(0,8):
    ano = int(input('Digite o ano de nascimento: '))
    if ano_atual - ano >= 18:
        maior += 1
    elif ano_atual - ano < 18:
        menor += 1

print(f' Maiores de idade: {maior} \n Menores de idade: {menor}')