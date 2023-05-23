print('----------------Olá, muito bem-vindo!-----------------')
print('''Nossas opções são: 
A - Álcool   - R$1,7997
D - Diesel   - R$0,9798
G - Gasolina - R$2.1009''')
tipo = input('Digite a letra A, D ou G para escolher o combustível a ser utilizado: ')
tipo= tipo.upper()
qtdLitros = float(input('Digite quantos litros deseja abastecer: '))

if tipo == 'A':
    valorpago = 1.7997 * qtdLitros
    print(f'O valor a ser pagor é {valorpago:.4f}')
elif tipo == 'D':
    valorpago = 0.9798 * qtdLitros
    print(f'O valor a ser pagor é {valorpago:.4f}')
elif tipo == 'G':
    valorpago = 2.1009 * qtdLitros
    print(f'O valor a ser pagor é {valorpago:.4f}')
else:
    print('Opção Inválida!')
