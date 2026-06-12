try:
    horario = str(input('Digite o horario: '))
    conversao = horario.replace(':','')
    conversao = int(conversao)
    if conversao >= 0 and conversao < 1200:
        print('Bom Dia!')
    elif conversao > 1200 and conversao <= 1800:
        print('Boa Tarde!')   
    else:
        conversao > 1800 and conversao <= 2300
        print('Boa Noite!')   
except ValueError:
    print('Comando incorreto, por favor insira o horario no formato H(horas):M(minutos) (H:M)')        