num = int(input('Digite o número: '))
soma = 0
resta = 0

while num != 0:
    resta = num % 10
    soma = soma + resta
    num = int(num/10)
print(f'a soma de todos os dígitos é de: {soma}')