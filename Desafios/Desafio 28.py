import random

aleatorio = random.randint(0 ,5)

print('-' * 85)
print(f'Vou escolher um numero de 0 a 5, e voce tem que tentar adivinhar qual é, vamos lá!')
print('-' * 85)

while  True:

    resposta = int(input('Tente adivinhar qual numero é: '))

    if resposta < aleatorio:
        print('Voce errou, o numero que pensei é maior.')
    elif resposta > aleatorio:
        print('Voce errou, o numero que pensei é menor.')   
    else:
        resposta == aleatorio
        print(f'BOA!! O numero que pensei, foi extamente o {aleatorio}. ')
        break     
        