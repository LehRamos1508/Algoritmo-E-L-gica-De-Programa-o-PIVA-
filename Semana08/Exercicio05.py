frase = input('Digite a frase: ')
arrayfrase = frase.split()

if len(arrayfrase) == 1:
    print(f'Essa fase possui {len(arrayfrase)} palavra!')
else:
    print(f'Essa fase possui {len(arrayfrase)} palavras!')