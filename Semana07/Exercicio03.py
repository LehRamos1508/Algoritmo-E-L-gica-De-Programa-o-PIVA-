total_pessoa = int(input('Quantas pessoas serão cadastradas? '))
peso_medio = 0
altura_media = 0
peso_total = 0
altura_total = 0
menor_IMC = 1000
maior_IMC = 0
for i in range(1, total_pessoa+1):
    peso= float(input(f'Digite o peso da {i}ª pessoa: '))
    altura = float(input(f'Digite a altura da {i}ª pessoa em metros: '))
    peso_total += peso
    altura_total += altura
    peso_medio = peso_total / total_pessoa
    altura_media = altura_total / total_pessoa
    imc = peso / (altura * altura)
    if imc < menor_IMC :
        menor_IMC = imc
    if imc > maior_IMC:
        maior_IMC = imc

print(f'O peso médio é {peso_medio:.1f} Kg')
print(f'A altura média é {altura_media:.1f} M')
print(f'O maior IMC é {maior_IMC:.1f}')
print(f'O menor IMC é {menor_IMC:.1f}')


