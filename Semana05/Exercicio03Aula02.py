preco = float(input('Digite aqui o preço líquido do produto <00.00>: '))
codigoOrigem = int(input('Digite o código de origem entre 1 e 5: '))

if (codigoOrigem == 1):
    codigoOrigem = 1 * 1.11
    print(f' O preço final do produto é R${preco*codigoOrigem:.2f}')
elif (codigoOrigem == 2):
    codigoOrigem = 1 * 1.13
    print(f' O preço final do produto é R${preco*codigoOrigem:.2f}')
elif (codigoOrigem == 3):
    codigoOrigem = 1 * 1.09
    print(f' O preço final do produto é R${preco*codigoOrigem:.2f}')
elif (codigoOrigem == 4):
    codigoOrigem = 1 * 1.12
    print(f' O preço final do produto é R${preco*codigoOrigem:.2f}')
elif (codigoOrigem == 5):
    codigoOrigem = 1 * 1.18
    print(f' O preço final do produto é R${preco*codigoOrigem:.2f}')
