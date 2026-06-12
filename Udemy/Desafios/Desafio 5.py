nome = str(input('Digite seu nome: ')).strip().split()

if len(nome[0]) <= 4:
    print(f'Seu primeiro nome {nome[0]} tem {len(nome[0])} letras, por isso seu nome é CURTO')

elif len(nome[0]) >= 5 and len(nome[0]) <= 6:
    print(f'Seu primeiro nome {nome[0]} tem {len(nome[0])} letras, por isso seu nome é NORMAL')
    
else:
    len(nome[0]) > 6
    print(f'Seu primeiro nome {nome[0]} tem {len(nome[0])} letras, por isso seu nome é GRANDE')  
