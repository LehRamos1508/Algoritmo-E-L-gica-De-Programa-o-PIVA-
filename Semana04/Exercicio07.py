deposito = float(input('Digite o valor do deposito: R$'))
taxa_Juros = float(input('Digite o percentual da taxa de juros: '))
valor_Rendimento = deposito * (taxa_Juros/100)
valor_total= valor_Rendimento+deposito
print(f'O valor do rendimento será de R${valor_Rendimento:.2f}. O valor total será de R${valor_total}.')