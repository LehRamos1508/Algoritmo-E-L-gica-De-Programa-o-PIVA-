nota = float(input('Digite uma nota que esteja entre 0 e 1: '))

if (nota < 0 or nota > 1):
    print('Entrada errada!')
elif (nota >= 0.9):
    print('Seu conceito é A')
elif (nota >= 0.8):
    print('Seu conceito é B')
elif (nota >= 0.7):
    print('Seu conceito é C')
elif (nota >= 0.6):
    print('Seu Conceito é D')
else:
    print('Seu conceito é F')
