nome = str(input('Digite seu nome: ')).strip()

divisao_nome = nome.split()
tamanho_nome = len(divisao_nome[0])

print(f'O nome {nome} com todas as letras maiusculas fica {nome.upper()}')
print(f'O nome {nome} com todas as letras minusculas fica {nome.lower()}')
print(f'O nome {nome} tem {len(nome)} caracteres')
print(f'O primeiro nome de {nome} tem {tamanho_nome} caracteres')
