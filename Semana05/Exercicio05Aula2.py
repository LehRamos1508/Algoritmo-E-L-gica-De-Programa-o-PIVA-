num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
media = (num1+num2)/2
diferenca = num1 - num2
diferenca = abs(diferenca)
produto = num1*num2
divisao = num1/num2

print('---------------------------------------------')
print("      Selecione a operação desejada")
print("1 - Média entre os números digitados")
print('2 - Diferença do maior pelo menor')
print('3 - Produto entre os números digitados')
print('4 - Divisão do primeiro pelo segundo')
opcao = int(input('Digite a opção desejada: '))

if (opcao == 1):
    print(f'A média entre os números digitados é: {media}')
elif(opcao == 2):
    print(f'A diferença do maior pelo menor é de: {diferenca}')
elif(opcao == 3):
    print(f'O produto entre os números digitados é de: {produto}')
elif(opcao== 4):
    print(f'A divisão do primeiro pelo segundo é de: {divisao:.2f}')
else:
    print('Você digitou uma opção inválida')