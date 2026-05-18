import random

aleatorio = random.randint(0 ,5)

while  True:

    resposta = int(input('Eu escolhi um numero de 0 a 5 e voce tem que descobrir qual numero é, entao digite qual numero voce acha que eu escolhi: '))
    
    if resposta < aleatorio:
        print('Voce errou, o numero que pensei é maior.')
    elif resposta > aleatorio:
        print('Voce errou, o numero que pensei é menor.')   
    else:
        resposta == aleatorio
        print(f'BOA!! O numero que pensei, foi extamente o {aleatorio}. ')
        break     
        