sal_atual = float(input('Digite o salário atual: R$'))
percentual_Aumento = float(input('Digite o percentual a ser acrescido ao salário: '))
percentual = percentual_Aumento/100
valor_aumento = sal_atual * (percentual)
novo_salario = sal_atual+valor_aumento
print(f'O valor do aumento será de R${valor_aumento:.2f}. O valor do novo salário será de R${novo_salario:.2f}')