x = int(input('Digite o primeiro número inteiro: '))
y = int(input('Digite o segundo número inteiro: '))

if (x>y):
    print(f'O número {y} é o menor entre os digitados.')
else:
    if (x==y):
        print(f'Os números {x} e {y} são iguais.')
    else:
        print(f'O número {x} é o menor entre os digitados.')