n1 = int(input('Digite um numero para ver quantos numeros pares tem ate ele: '))
print(f'Os numeros pares ate o numero {n1} são: ')
for c in range(0,n1 + 2):
    if c % 2 == 0:
        print(f'N° {c}')