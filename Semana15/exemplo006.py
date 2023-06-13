with open('frutas.txt', 'w', encoding='utf-8') as arquivo:
    while True:
        fruta = input('Digite uma fruta: ')
        if fruta == 'sair':
            break
        else:
            arquivo.write(f'- {fruta}\n')

# arquivo = open('frutas.txt', 'r', encoding='utf-8')
# texto = arquivo.read()
# print(texto)

# arquivo.close()
