fibo = int(input('Quantos números da sequência Fibonacci devo calcular? '))
x = 0
y = 1
print(f'- {x} - {y} - ', end='')
for i in range(0, fibo-2):
    z = x + y
    x = y
    y = z
    print(f'{z} - ', end='')
