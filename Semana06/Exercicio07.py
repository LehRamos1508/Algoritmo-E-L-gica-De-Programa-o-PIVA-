dolar = input('Qual a cotação atual do dolar: $')
dolar = dolar.replace(",", ".")
dolar = float(dolar)
pontos_Necessarios = float(input('Qual a quantidade de pontos necessárias para resgatar o produto (em mil unidades): '))
pontos_dolar = 1.5
gasto_dolar = pontos_Necessarios/1.5
gasto_real = gasto_dolar * dolar
print(f'Para resgatar esse produto você deverá gastar R${gasto_real:.2f} ')