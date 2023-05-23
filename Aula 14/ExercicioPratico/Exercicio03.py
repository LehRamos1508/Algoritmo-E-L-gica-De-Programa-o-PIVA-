ra = input('Digite aqui o seu RA com 13 dígitos (0000000000000): ')
multiplicacao = 1
soma = 0

for digito in ra:
    multiplicacao *= int(digito)
    soma += int(digito)

print(f'Multiplicação = {multiplicacao}')
print(f'soma = {soma}')
