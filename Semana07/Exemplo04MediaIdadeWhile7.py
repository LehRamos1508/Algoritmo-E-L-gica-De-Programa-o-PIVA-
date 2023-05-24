idade = 0
soma = 0
qtd = 0

while idade != 1000:
    idade = int(input(f'Digite a {qtd+1}ª idade: '))
    if idade !=1000:
        soma += idade   #mesma coisa que soma= soma + idade
        qtd= qtd + 1

if qtd == 0:
    print('Não foi digitada idade alguma.')
else:
    media = soma / qtd
    print(f'A média das {qtd} idades é : {media}.')