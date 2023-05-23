def num_primo(n):
    if n > 1:
        for i in range (2 , n):
            if n % i == 0:
                return False
            else:
                return True

def primo(n):
    numeros_primos = []
    for i in range(0, n+1):
        if num_primo(i):
            numeros_primos.append(i)

    return(numeros_primos)

n = int(input('Digite um valor: '))

if n > 1:
    if num_primo(n):
        print(f'{n} é primo')
    else:
        print(f'Não é primo')

soma = 0

listaprimos = primo(n)
for i in range(0, n+1):
    if num_primo(i):
        soma += i
print(listaprimos)
print(f'Soma dos números primos é {soma}')
