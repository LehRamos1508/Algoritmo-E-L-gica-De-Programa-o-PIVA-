nota = float(input('Digite uma nota que esteja entre 0 e 1: '))

if (nota < 0 or nota > 1):
    print('Entrada errada!')
else:
    if (nota >= 0.9):
        print('Seu conceito é A')
    else:
        if (nota >= 0.8):
            print('Seu conceito é B')
        else:
            if (nota >= 0.7):
                print('Seu conceito é C')
            else:
                if (nota >= 0.6):
                    print('Seu Conceito é D')
                else:
                    print('Seu conceito é F')
