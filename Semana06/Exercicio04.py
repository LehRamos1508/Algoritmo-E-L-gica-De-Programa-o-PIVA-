num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))
soma = num1+num2

if soma < 1000:
    print(f'''A soma desses dois números é igual a = {soma}.
Esse número é menor que 1000 (Mil)''')
elif soma > 1000:
    print(f'''A soma desses dois números é igual a = {soma}.
Esse número é maior que 1000 (Mil)''')
else:
    print(f'A soma desses dois números é igual a = {soma}.')