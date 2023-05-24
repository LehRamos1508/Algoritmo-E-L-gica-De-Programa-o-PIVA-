numero = int(input('Digite um número inteiro posítivo: '))
fatorial = 1
if numero < 0:
    print('Não existe fatorial de números negativos')
elif numero == 0:
    print('Fatorial de 0 é igual a 1')
else:
    for i in range (1, numero+1):
        fatorial = fatorial * i
    print(f'O fatorial de {numero} é igual a {fatorial}.')