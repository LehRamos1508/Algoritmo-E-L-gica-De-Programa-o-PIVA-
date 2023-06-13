vet1, vet2, vetResultante = [], [], []

for i in range(5):
    num1 = float(input(f'VETOR 1: Digite o {i+1}º número: '))
    vet1.append(num1)

print('='*30)

for x in range(5):
    num2 = float(input(f'VETOR 2: Digite o {x+1}º número: '))
    vet2.append(num2)

for z in range(5):
    vetResultante.append(vet1[z])
    vetResultante.append(vet2[z])

print(f'Vetor 1 = {vet1}')
print(f'Vetor 2 = {vet2}')
print(f'Vetor resultante = {vetResultante}')