import random

nomes = []

for c in range(1,5):
    nome = str(input('Digite o nome do aluno: '))
    nomes.append(nome)

random.shuffle(nomes)    

print(f'A seguinte ordem de apresentação dos alunos será: {nomes}')   