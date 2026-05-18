nome = str(input('Digite seu nome completo: ')).split()

ultimo = nome[-1]
primeiro = nome[0]

print(f' Primeiro nome = {primeiro} \n Ultimo nome = {ultimo:>6}')
