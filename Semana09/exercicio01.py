vetor = []

for i in range(10):
    num = int(input(f'Digite {i+1}º número inteiro: '))
    vetor.append(num)

print(f'Ordem de entrada: {vetor}')

vetor.reverse()
print(f'Ordem inversa de entrada: {vetor}')