from random import randint
arrayContagem = [0]*11
cont2, cont3, cont4, cont5, cont6, cont7, cont8, cont9, cont10, cont11, cont12 = 0,0,0,0,0,0,0,0,0,0,0

for i in range(30000):
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    soma = dado1 + dado2

    if soma == 2:
        cont2 += 1
        arrayContagem[0] = cont2

    if soma == 3:
        cont3 += 1
        arrayContagem[1] = cont3

    if soma == 4:
        cont4 += 1
        arrayContagem[2] = cont4

    if soma == 5:
        cont5 += 1
        arrayContagem[3] = cont5
        
    if soma == 6:
        cont6 += 1
        arrayContagem[4] = cont6

    if soma == 7:
        cont7 += 1
        arrayContagem[5] = cont7

    if soma == 8:
        cont8 += 1
        arrayContagem[6] = cont8

    if soma == 9:
        cont9 += 1
        arrayContagem[7] = cont9

    if soma == 10:
        cont10 += 1
        arrayContagem[8] = cont10

    if soma == 11:
        cont11 += 1
        arrayContagem[9] = cont11

    if soma == 12:
        cont12 += 1
        arrayContagem[10] = cont12

print(arrayContagem)
print(f'A frequência do número 2 é igual a {((arrayContagem[0] * 100) / i):.2f}%')
print(f'A frequência do número 3 é igual a {((arrayContagem[1] * 100) / i):.2f}%')
print(f'A frequência do número 4 é igual a {((arrayContagem[2] * 100) / i):.2f}%')
print(f'A frequência do número 5 é igual a {((arrayContagem[3] * 100) / i):.2f}%')
print(f'A frequência do número 6 é igual a {((arrayContagem[4] * 100) / i):.2f}%')
print(f'A frequência do número 7 é igual a {((arrayContagem[5] * 100) / i):.2f}%')
print(f'A frequência do número 8 é igual a {((arrayContagem[6] * 100) / i):.2f}%')
print(f'A frequência do número 9 é igual a {((arrayContagem[7] * 100) / i):.2f}%')
print(f'A frequência do número 10 é igual a {((arrayContagem[8] * 100) / i):.2f}%')
print(f'A frequência do número 11 é igual a {((arrayContagem[9] * 100) / i):.2f}%')
print(f'A frequência do número 12 é igual a {((arrayContagem[10] * 100) / i):.2f}%')

if (arrayContagem[5] > 5000):
    print('O valor 7 corresponde a mais de 1/6 das jogadas!')
else:
    print('O valor 7 não corresponde a 1/6 das jogadas!')