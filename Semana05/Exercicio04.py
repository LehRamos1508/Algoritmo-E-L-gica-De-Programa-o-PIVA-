h = float(input('Digite sua altura em M (0.00): '))
sexo = input('Qual o seu sexo? ("M" ou "F"): ')
sexo = sexo.upper()
homem = (72.7 * h) - 58
mulher = (62.1 *h) - 44.7

if (sexo == 'M'):
    print(f'Seu peso ideal é {homem:.2f} quilos.')
else:
    print(f'Seu peso ideal é {mulher:.2f} quilos.')