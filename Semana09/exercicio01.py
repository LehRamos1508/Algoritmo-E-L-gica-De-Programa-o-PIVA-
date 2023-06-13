v = []

for i in range(10):
    num = int(input(f' Digite o {i+1}º número inteiro: '))
    vetor.append(num)

print(f'Entrada: {vetor}')

vetor.reverse()
print(f'Ordem inversa: {vetor}')
