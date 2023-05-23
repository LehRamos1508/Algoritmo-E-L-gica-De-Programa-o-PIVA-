fruta = input('Digite o Nome da fruta: ')
fruta = fruta.lower()

if (fruta == 'banana'):
    print('O Kg da banana está R$5,23')
elif (fruta == 'maça'):
    print('O Kg da maçã está R$12,10')
elif (fruta == 'cereja'):
    print('O Kg da cereja está R$58,00')
else:
    print(f'Desculpe, mas no momento não possuímos {fruta} em nosso estoque')