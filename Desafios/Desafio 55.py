maior = 0


for c in range(0 ,5):
    peso = float(input('Digite o peso: '))
    menor = peso

    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso 
            

print(f' O maior peso digitado foi: {maior:.1f} \n e o menor peso digitado foi: {menor:.1f}')        