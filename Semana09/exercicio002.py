vetor = []

for i in range(10):
    num = int(input(f'Digite o {i + 1}º número:'))
    vetor.append(num)

maiorNumero = max(vetor)
posicao = vetor.index(maiorNumero)

print(f'Vetor: {vetor}')
print(f'Maior número do vetor: {maiorNumero}\nIdex do maior número: {posicao}')
