import random

nome1 = str(input('Digite o nome do primeiro aluno: '))
nome2 = str(input('Digite o nome do segundo aluno: '))
nome3 = str(input('Digite o nome do terceiro aluno: '))
nome4 = str(input('Digite o nome do quarto aluno: '))

sorteado = random.randint(1, 4)

if sorteado == 1:
    print(f'Aluno(a) sorteado(a) {nome1}')
elif sorteado == 2:
    print(f'Aluno(a) sorteado(a) {nome2}')
elif sorteado == 3:
    print(f'Aluno(a) sorteado(a) {nome3}')
elif sorteado == 4:
    print(f'Aluno(a) sorteado(a) {nome4}')            