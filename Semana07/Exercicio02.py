n = 2
soma = 0
while True:
    if (n % 2 == 1):
        n += 1
        continue
    soma += n
    n += 1
    if n > 100:
        break
print(f'A soma dos primeiros 50 números pares é de {soma}')