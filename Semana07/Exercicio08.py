num = int(input('Digite um número inteiro e maior que 1: '))
contador = 0
if num > 1:
    for i in range(1, num+1):
        if num % i == 0:
            contador += 1
    if contador == 2:
        print(f'O número {num} é primo!')
    else:
        print(f'O número {num} não é primo!')
else:
    print('Número inválido!')


