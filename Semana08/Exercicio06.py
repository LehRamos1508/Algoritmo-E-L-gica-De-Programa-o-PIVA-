frase = input('Digite algo para verificar se é palíndromo: ')
frase = frase.lower()
fraseInverso = ''
for i in frase[::-1]:
    fraseInverso += i

if (frase == fraseInverso):
    print(f'{frase} é PALÍNDROMO!')
else:
    print(f'{frase} não é PALÍNDROMO!')