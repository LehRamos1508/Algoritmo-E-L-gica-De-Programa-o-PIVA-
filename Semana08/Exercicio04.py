frase = input('Digite uma frase: ')
cont_Vogais = 0
frase2 = frase.lower()

for i in frase2:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        cont_Vogais += 1

print(f'A frase "{frase}" possui {cont_Vogais} vogais!')