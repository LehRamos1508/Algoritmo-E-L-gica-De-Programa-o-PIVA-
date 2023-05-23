compra = float(input('Qual o valor da compra? R$'))
valorDesconto = 0
valorFinalCompra = 0
if compra <= 1000:
    valorDesconto = compra - compra * 0.9
    valorFinalCompra = compra * 0.9
elif compra > 1000 and compra <= 5000:
    valorDesconto = compra - compra * 0.80
    valorFinalCompra = compra * 0.80
else:
    valorDesconto = compra - compra * 0.70
    valorFinalCompra = compra * 0.70

print(f'O valor total do desconto é de R${valorDesconto:.2f}')
print(f'O valor da final da compra é de R${valorFinalCompra:.2f}' )