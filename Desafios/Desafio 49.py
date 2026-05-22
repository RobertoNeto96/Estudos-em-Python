n1 = int(input('Digite um numero para ver sua tabuada: '))

for c in range(0,10 + 1):
    print(f'{n1:<2} X {c:>2} = {n1 * c:>2}')