idade, cont, somaIdade = 1, 1, 0
while True:
    print('Se deseja sair digite idade = 0')
    idade = int(input(f'Digite a {cont}ª idade: '))
    if idade == 0:
        break
    else:
        somaIdade += idade
        media =  somaIdade / cont
        cont += 1

print(f'A idade média do grupo é {media:.2f}. O total de pessoas é {cont-1}')


