arquivo = open('frutas.txt', encoding='utf-8')
texto = arquivo.read().strip()
lista = texto.split('\n')
print(lista)
arquivo.close()

arquivo = open('frutas.txt', 'a', encoding='utf-8')
while True:
    fruta = input('Digite uma fruta: ')
    if fruta == '':
        break
    elif fruta in lista:
        print('Fruta repetidade!!!')
    else:
        arquivo.write(f'{fruta}\n')

arquivo.close()