nota1 = float(input('Digite o valor da primeira nota: '))
nota2 = float(input('Digite o valor da segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 7 and media <= 9.9:
    print(f'Parabens! com a média de {media} pontos você esta APROVADO!')
elif media >= 5 and media <= 7.9:
    print(f'Com a media de {media} pontos, voce esta de RECUPERAÇÃO! ')
elif media < 5:
    print(f'Com a média de {media} pontos, voce esta REPROVADO! ')    
else:
    media == 10
    print(f'UAU você teve média de {media} pontos, PARABENS voce foi aprovado com 100% de aprovação')        