def listaPrimos(numeroDoUsuario):
    listaNumerosPrimos = []
    cont, i = 0, 0 
    while cont < numeroDoUsuario:
        i += 1
        primo = primoOuNao(i)
        if primo:
            listaNumerosPrimos.append(i)
            cont += 1

    return listaNumerosPrimos


def primoOuNao(numero):
    cont = 0
    for i in range(1, numero+1):
        if numero % i == 0:
            cont += 1
    
    if cont == 2:
        return True
    else:
        return False

num = int(input('Digite um número: '))
arrayPrimos = listaPrimos(num)
somaDosNumerosPrimos = 0

for i in arrayPrimos:
    somaDosNumerosPrimos += i

print(f'\nLista dos números primos até {num}: \n{arrayPrimos}')
print(f'\nA soma de todos os números primos presentes na lista é igual a {somaDosNumerosPrimos}!')