for c in range(0,4):

    maior = ''
    menores = 0

    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [Feminino/Masculino] \n ')).upper()

    soma = idade + idade
    media = soma / 4

    if 'M MASCULINO' in sexo and idade > maior:
        maior == nome

    if 'S FEMININO' in sexo and idade < 20:
        menores += 1     

print(f'A media de idade do grupo é: {media} \n O homem mais velho é: {maior} \n e o total de mulheres abaixo de 20 anos é {menores}')