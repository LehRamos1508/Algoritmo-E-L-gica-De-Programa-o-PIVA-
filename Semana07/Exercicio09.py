b = int(input('Digite o primeiro valor inteiro e positivo: '))
n = int(input('Digite o segudo valor inteiro e positivo: '))
soma = 0

for i in range(1, n+1):
    soma += (b ** i)

print(f'E = {soma}')

c = int(input('Digite o primeiro valor inteiro e positivo: '))
d = int(input('Digite o segudo valor inteiro e positivo: '))
cont, soma = 1, 0

# while cont <= d:
#     soma += (c**cont)
#     cont +=1
# print(f'E = {soma}')
