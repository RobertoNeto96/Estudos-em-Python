cadastro_senha = str(input('Digite sua senha: '))
tentativa = 3

print('_-_' * 10 , 'Vamos entrar no sistema' , '_-_' * 10)

while True:
    login = str(input('Digite sua senha: '))

    if cadastro_senha == login:
        print('Bem vindo ao nosso sistema')
    else:
        cadastro_senha != login
        tentativa -= 1
        print(f'Senha incorreta, voce tem mais {tentativa} tentativas') 
    if tentativa <= 0:
        print('Tentativas de login excedidas.')
        break       