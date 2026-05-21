from datetime import datetime

cores = {'vermelho':'\033[1;31m', 
         'amarelo':'\033[1;33m', 
         'verde':'\033[1;32m',
         'azul':'\033[1;34m',
         'magenta':'\033[1;35m',
         'saida':'\033[m'}

nome = str(input('Digite seu nome: ')).strip().title()
nascimento_entrada = str(input('Digite sua data de nascimento (dd/mm/aaaa): ')).strip()

nascimento = nascimento_entrada.replace('/',' ').split()
ano_nascimento = int(nascimento[2]) 
ano_atual = datetime.today().year
idade = ano_atual - ano_nascimento

print('-.-' * 30)
print(f'{'CATEGORIAS':^90}')
print('-.-' * 30)

print(f'{' De 2 a 9 anos':.<35} {cores['verde']}{'JUVENIL':<}{cores['saida']}                            \n {'De 10 a 14 anos':.<35} {cores['azul']}{'INFANTIL':<}{cores['saida']}                               \n {'De 15 a 19 anos':.<35} {cores['amarelo']}{'JUNIOR':<}{cores['saida']}                              \n {'De 20 a 21 anos':.<35} {cores['magenta']}{'SENIOR':<}{cores['saida']}                              \n {'A partir de 21 anos':.<35} {cores['vermelho']}{'MASTER':<}{cores['saida']}')

print('-.-' * 30)

if idade >= 2 and idade <= 9:
    print(f'{nome} Sua categoria é: \033[1;32mJUVENIL\033[m')

elif idade >= 10 and idade <= 14:
    print(f'{nome} Sua categoria é: \033[1;34mINFANTIL\033[m')

elif idade >= 15 and idade <= 19:
    print(f'{nome} Sua categoria é: \033[1;33mJUNIOR\033[m')

elif idade >= 20 and idade <= 21:
    print(f'{nome} Sua categoria é: \033[1;35mSENIOR\033[m')

else:
    idade > 21
    print(f'{nome} Sua categoria é: \033[1;31mMASTER\033[m')                

