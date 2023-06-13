numeroString = input('Digite um número: ')
soma, multiplicacao = 0, 1
for i in numeroString:
    numeroInt = int(i)
    soma += numeroInt
    multiplicacao *= numeroInt

print(f'A soma de todos os dígitos do número {numeroString} é igual a {soma}!')
print(f'A multiplicação de todos os dígitos do número {numeroString} é igual a {multiplicacao}!')