sal_Minimo = float(input('Digite o valor do salário mínimo atual: R$'))
qtd_klwt = float(input('Digite o valor de quilowatts consumido: '))
custo_Klwt = sal_Minimo/8
valor_Pago = qtd_klwt*custo_Klwt
valor_Desconto = valor_Pago * 0.85

print(f'O valor de cada quilowatt é de R${custo_Klwt:.2f}')
print(f'O valor a ser pago é de R${valor_Pago:.2f}')
print(f'O valor a ser pago com desconto é de R${valor_Desconto}')
#O valor do KW no exercício parece bem descolado da realidade