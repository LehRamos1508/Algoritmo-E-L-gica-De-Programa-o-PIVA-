def parOuNão (num):
    return (num % 2 == 0)
      

cont = 0
i = 1
while cont < 10:
    par = parOuNão(i)
    if par:
        cont += 1
        print(f'{i} - ', end='')
    i+=1