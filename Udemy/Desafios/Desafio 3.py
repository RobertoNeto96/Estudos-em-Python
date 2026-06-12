while True:
    try:
        entrada = int(input('Digite um numero inteiro: '))

        if entrada % 2 == 0:
            print('O numero digitado é PAR')
            cont = str(input('Quer verificar outro numero? [S/N]' )).upper()
            if cont == 'N':
                print('Obrigado por usar nosso sistema, volte sempre!')
                break
        else:
            print('O numero digitado é IMPAR')
            cont = str(input('Quer verificar outro numero? [S/N]' )).upper()
            if cont == 'N':
                print('Obrigado por usar nosso sistema, volte sempre!')
                break
    except ValueError:
        print('Numero invalido, digite um numero sem pontos ou virgulas.')            
