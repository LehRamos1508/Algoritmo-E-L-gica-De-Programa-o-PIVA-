lista1, listaInversa = [], []

for i in range(10):
    num = int(input(f'Digite o {i+1}º número: '))
    lista1.append(num)

tupla = tuple(lista1)

listaInversa = list(tupla)
listaInversa.sort()

tuplaInversa = tuple(listaInversa)

print(f'Tupla original: {tupla}')
print(f'Tupla em ordem inversa: {tuplaInversa}')
