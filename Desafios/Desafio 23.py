numero = str(input('Digite um numero de 0 a 9999: '))

if len(numero) == 4:
    unidade = numero[3]
    dezena = numero[2]
    centena = numero[1]
    milhar = numero[0]
    print(f' Milhar:  {milhar} \n centena: {centena} \n dezena:  {dezena} \n unidade: {unidade}')
elif len(numero) == 3:
    centena = numero[0]
    dezena = numero[1]
    unidade = numero[2]
    print(f' centena: {centena} \n dezena:  {dezena} \n unidade: {unidade}')
elif len(numero) == 2:
    dezena = numero[0]
    unidade = numero [1]
    print(f' dezena:  {dezena} \n unidade: {unidade}')
else:
    len(numero) == 1
    unidade = numero 
    print(f'unidade: {unidade}')

# DESAFIO RESOLVIDO MATEMATICAMENTE

#unidade = numero % 10
#dezena = (numero // 10) % 10
#centena = (numero // 100) % 10
#milhar = (numero // 1000) % 10

#print(f' Unidade:{unidade:>2} \n Dezena:{dezena:>3} \n Centena:{centena:>2} \n Milhar:{milhar:>3}')