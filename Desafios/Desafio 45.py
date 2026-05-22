import random  

print('-.-' * 30)
print(f'{'Vamos jogar PEDRA, PAPEL ou TESOURA!':>60}')
print('-.-' * 30)

while True:
    maquina = random.randint(1, 3)    
    jogador = int(input('Escolha! \n [1] PEDRA \n [2] PAPEL \n [3] TESOURA \n  '))

    if jogador == 1 and maquina == 2:
        print(f'Que pena, voce escolheu PEDRA e eu escolhi PAPEL, entao eu venci!')
    elif jogador == 1 and maquina == 3:
        
        print(f'UAU, voce escolheu PEDRA e eu escolhi TESOURA, entao voce venceu!!')
    elif jogador == 1 and maquina == 1:
        print(f'OPA! voce escolheu PEDRA e eu tambem, nós empatamos.')

    if jogador == 2 and maquina == 3:
        print(f'Que pena, voce escolheu PAPEL e eu escolhi TESOURA, entao eu venci!')
    elif jogador == 2 and maquina == 1:
        print(f'UAU, voce escolheu PAPEL e eu escolhi PEDRA, entao voce venceu!!')
    elif jogador == 2 and maquina == 2:
        print(f'OPA! voce escolheu TESOURA e eu tambem, nós empatamos.')             

    if jogador == 3 and maquina == 1:
        print(f'Que pena, voce escolheu TESOURA e eu escolhi PEDRA, entao eu venci!')
    elif jogador == 3 and maquina == 2:
        print(f'UAU, voce escolheu TESOURA e eu escolhi PAPEL, entao voce venceu!!')
    elif jogador == 3 and maquina == 3:
        print(f'OPA! voce escolheu PEDRA e eu tambem, nós empatamos.')   

    cont = str(input('Quer jogar novamente? [S/N] \n ')).upper()
    if cont == 'N':
        break
 