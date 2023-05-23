idade = int(input('Digite a idade do nadador: '))

if (idade >= 5 and idade <= 7):
    print('Esse nadador pertence a categoria INFANTIL.')
elif (idade >= 8 and idade <= 10):
    print('Esse nadador pertence a categoria JUVENIL.')
elif (idade >= 11 and idade <= 15):
    print('Esse nadador pertence a categoria ADOLESCENTE.')
elif (idade >= 16 and idade <= 30):
    print('Esse nadador pertence a categoria ADULTO.')
elif (idade > 30):
        print('Esse nadador pertence a categoria SÊNIOR.')
else:
    print('Infelizmente não contamos com categoria para esse idade.')