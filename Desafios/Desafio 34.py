salario_entrada = str(input('Digite seu salario: '))

salario = salario_entrada.replace(',','.').replace('.','')
salario = float(salario)

if salario > 1250:
    aumento = (salario * 0.10) + salario
    print(f'Com o salario de R${salario:.2f} Reais você tem direito de um aumento de 10%. Seu novo salario passa a ser R${aumento:.2f} Reais')
else:
    salario <= 1250
    aumento = (salario *0.15) + salario 
    print(f'Com o salario de R${salario:.2f} Reais você tem direito de um aumento de 15%. Seu novo salario passa a ser R${aumento:.2f} Reais')   