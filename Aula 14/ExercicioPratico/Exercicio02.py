def num_primo(n):
    if n > 1:
        for i in range (2 , n):
            if n % i == 0:
                return False
            else:
                return True

def primo(n):
    numeros_primos = []
    cont, i = 0, 0
    while cont < n:
        i += 1
        p = num_primo(i)
        if p:
            numeros_primos.append(i)
            cont += 1
    return(numeros_primos)

n = int(input('Digite um valor: '))

if n > 1:
    if num_primo(n):
        print(f'{n} é primo')
    else:
        print(f'Não é primo')

soma = 0

listaprimos = primo(n)

print(listaprimos)
print(f'Soma dos números primos é {sum(listaprimos)}')
