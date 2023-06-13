lista = []

for i in range(5):
    listaModelo = []
    print(f'Veículo {i+1}')
    nome = input('Nome: ')
    KmLitro = int(input('Km por Litro: '))
    listaModelo.append(KmLitro)
    listaModelo.append(nome.upper())
    lista.append(listaModelo)

lista.sort()

print('\nRelatório Final...\n')

for x in lista:
    kmLitro = x[0]
    nomeCarro = x[1]
    consumoMilKm = (1000 / kmLitro) 
    precoMilKm = consumoMilKm * 5.65

    print(f'- {nomeCarro:10} - {kmLitro:6.1f} - {consumoMilKm:6.2f} litros - R$ {precoMilKm:.2f}')

print(f'\nO menor consumo é do modelo {lista[-1][1]}')