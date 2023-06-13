from random import randint
array = []

def primoOuNao (num):
    cont = 0
    for i in range(1, num + 1):
        if num % i == 0:
          cont += 1
    if cont == 2:
        return True
    else:
        return False
    
cont = 0
while cont < 10:
    num = randint(1, 1000)
    primo = primoOuNao(num)
    if primo:
        if num > 100:
            array.append(num)
            cont+=1

print(array)