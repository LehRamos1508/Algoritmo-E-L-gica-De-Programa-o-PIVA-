num = input('Digite o número: ')
soma = 0
mult = 1

for i in num:
    soma += int(i)
    mult *= int(i)
print(f'a soma de todos os dígitos é de: {soma}')
print (mult)