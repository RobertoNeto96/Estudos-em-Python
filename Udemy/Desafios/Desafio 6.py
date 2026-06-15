print('CALCULADORA \n \n ')

while True:
    try:
        n1 = float(input('Primeiro Numero   '))

        operador = str(input('[/]  [*]  [+]  [-]  '))  

        n2 = float(input('Segundo Numero    ')) 

        if operador == '/':
            resultado = n1 / n2
            print(resultado)
        elif operador == '*':
            resultado = n1 * n2
            print(resultado) 
        elif operador == '+':
            resultado = n1 + n2
            print(resultado) 
        elif operador == '-':
            resultado = n1 - n2
            print(resultado) 

        cont = str(input('Continuar? [S/N]')).upper()
        if cont != 'S' and cont != 'N':
            print('Comando incorreto, responda com S ou N ')
        elif cont == 'S':
            continue
        else:
            cont == 'N'
            print('Obrigado por usar nossa calculadora, volte sempre!')
            break             
    except ValueError:
        print('Utilize somente numeros! ')    