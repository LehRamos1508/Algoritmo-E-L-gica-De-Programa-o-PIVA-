lista1, lista2 = [], []

for _ in range(5):
    num = int(input('Digite um número para a primeira lista: '))
    lista1.append(num)

for _ in range(5):
    num = int(input('Digite um número para a segunda lista: '))
    lista2.append(num)

conjunto1 = set(lista1)
conjunto2 = set(lista2)
uniaoConjuntos = conjunto1.union(conjunto2)

print(f'Conjunto 1: {conjunto1}')
print(f'Conjunto 2: {conjunto2}')
print(f'União entre o Conjunto 1 e Conjunto 2: {uniaoConjuntos}')