array, arrayPalavrasInvertidas = [], []

for i in range(5):
    palavra = input('Digite uma palavra de no máximo 10 caracteres: ')
    if len(palavra) > 10:
        palavra = input('A palavra digitada ultrapassou 10 caracteres. Digite uma nova palavra: ')
    array.append(palavra)

for i in array:
    novaPalavra = ''
    for x in i[::-1]:
        novaPalavra += x
    arrayPalavrasInvertidas.append(novaPalavra)

print(array) 
print(arrayPalavrasInvertidas) 
        
    

