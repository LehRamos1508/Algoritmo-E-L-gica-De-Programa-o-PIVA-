soma = 0
for i in range(1, 6):
    idade = int(input(f'Digite a idade {i}: '))
    soma = soma + idade
media = soma/5
print('A média das idades é: ', media)