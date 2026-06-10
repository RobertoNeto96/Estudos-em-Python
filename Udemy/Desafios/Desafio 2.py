'''Desafio para praticar fatiamento e tratamento de strings'''

nome = str(input('Digite seu nome: ')).strip().upper()
idade = str(input('Digite sua idade: '))

if nome == '' and idade == '':
    print('Desculpe voce deixou campos vazios.')
else:
    print(f'Seu nome é: {nome}')  

    print(f'Seu nome invertido fica: {nome[::-1]}')
    if ' ' in nome:
        print(f'Seu nome contem espaços')
    else:
        print('Seu nome nao contem espaços') 

    print(f'Seu nome tem: {len(nome)} letras')  

    print(f'A primeira letra do seu nome é: {nome[0]}')

    print(f'A ultima letra do seu nome é: {nome[-1]}')