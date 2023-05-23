import math
num = float(input('Digite um número maior que zero: '))

if num <= 0:
    num= float(input("O número precisa ser maior que zero"))
else:
    print('O número digitado ao quadrado será: ', num**2)
    print('O número digitado ao cubo será: ', num**3)
    print('A raiz quadrada do número digitado é', math.sqrt(num))

