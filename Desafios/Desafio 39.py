from datetime import datetime

nascimento = int(input('Digite o seu ano de nascimento: '))

ano_atual = datetime.today().year
idade = ano_atual - nascimento

if idade < 18:
    print(f'Você tem {idade} anos, faltam { 18 - idade} ano(s) para poder se alistar')
elif idade == 18:
    print(f'Voce esta com {idade} anos, e tem que se alistar ')
else:
    idade > 18
    print(f'Voce já passou {idade - 18} ano(s) do alistamento obrigatório, vá ate a junta militar mais proxima. ')    