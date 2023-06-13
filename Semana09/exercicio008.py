from random import randint
vetorA, vetorB = [], []

for _ in range(10):
    num = randint(1,100)
    vetorA.append(num)

vetorB = vetorA[:]
vetorB.sort()

print(f'Vetor A: {vetorA}')
print(f'Vetor B: {vetorB}')