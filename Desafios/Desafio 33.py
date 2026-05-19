n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

maior = 0
menor = 0

if n1 > n2 and n1 > n3:
    maior = n1
elif n1 < n2 and n1 < n3:
    menor = n1 

if n2 > n1 and n2 > n3:
    meior = n2
elif n2 < n1 and n2 < n3:
    menor = n2 

if n3 > n1 and n3 > n2:
    maior = n3
elif n3 < n1 and n3 < n2:
    menor = n3

print(f'O maior numero é {maior} e o menor numero é {menor}')        