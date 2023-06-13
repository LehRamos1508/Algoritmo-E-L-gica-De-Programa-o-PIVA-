texto = input('Digite um texto: ')
arquivo = open('texto.txt', 'w', encoding='utf-8')
arquivo.write(texto)
arquivo.close()