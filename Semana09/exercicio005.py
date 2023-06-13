from random import randint

def frequencia(cont):
  return cont * 100 / 6000


cont1, cont2, cont3, cont4, cont5, cont6 = 0,0,0,0,0,0

for _ in range(6000):
    numero = randint(1, 6)

    if numero == 1:
        cont1 += 1

    if numero == 2:
        cont2 += 1

    if numero == 3:
        cont3 += 1

    if numero == 4:
        cont4 += 1

    if numero == 5:
        cont5 += 1

    if numero == 6:
        cont6 += 1

freqNum1 = frequencia(cont1)
freqNum2 = frequencia(cont2)
freqNum3 = frequencia(cont3)
freqNum4 = frequencia(cont4)
freqNum5 = frequencia(cont5)
freqNum6 = frequencia(cont6)

print(
    f'Dos 6000 lançamentos de dados: '
    f'\nNúmero 1: {freqNum1:.2f}% / {cont1} lançamentos'
    f'\nNúmero 2: {freqNum2:.2f}% / {cont2} lançamentos'
    f'\nNúmero 3: {freqNum3:.2f}% / {cont3} lançamentos'
    f'\nNúmero 4: {freqNum4:.2f}% / {cont4} lançamentos'
    f'\nNúmero 5: {freqNum5:.2f}% / {cont5} lançamentos'
    f'\nNúmero 6: {freqNum6:.2f}% / {cont6} lançamentos'
)