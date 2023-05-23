nota = float(input('Digite uma nota que esteja entre 0 e 1: '))

if (nota >= 0 and nota <= 1):
    if(nota >= 0.9):
        print('Seu conceito é A')
    elif (nota >= 0.8):
        print('Seu conceito é B')
    elif (nota >= 0.7):
        print('Seu conceito é C')
    elif (nota >= 0.6):
        print('Seu Conceito é D')
    else:
        print('Seu conceito é F')
else:
    print('Entrada errada!')
