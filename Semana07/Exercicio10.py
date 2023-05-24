base = float(input('Digite a base do triângulo: '))
while base <=0:
    print('Entrada inválida! Não são permitidas medidas menor ou iguais a 0 ')
    base = float(input('Digite a base do triângulo: '))

altura = float(input('Digite a altura do triângulo: '))
while altura <=0:
    print('Entrada inválida! Não são permitidas medidas menor ou iguais a 0 ')
    altura = float(input('Digite a altura do triângulo: '))

area = (base * altura) / 2
print(f'A área desse triângulo é: {area}')







#Área = (base x altura) / 2