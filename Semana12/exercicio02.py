def primoOuNão (num):
    cont = 0
    for i in range(1, num+1):
        if num % i == 0:
            cont+= 1
    return cont == 2

cont = 0
i = 0
while cont < 50:
    primo = primoOuNão(i)
    if primo:
        cont += 1
        print(f'{i} - ', end='')
    i+=1