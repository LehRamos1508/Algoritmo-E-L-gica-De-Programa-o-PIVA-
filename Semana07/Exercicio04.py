n = 0
total = 0
vezes = 0
while True:
    n = int(input('Digite um número inteiro: '))
    if n == 0:
        break
    if n % 2 == 0:
        total += n
        vezes += 1
        n = 0
    elif n % 2 == 1:
        print('Esse número é impar, portanto não será adicionado a média!')
        n = 0
media = total / vezes
print(f'A média aritmética do conjunto de números pares que foram fornecidos é {media:.2f}')

