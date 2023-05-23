x = float(input('Digite valor do primeiro lado: '))
y = float(input('Digite valor do segundo lado: '))
z = float(input('Digite valor do terceiro lado: '))

if (x+y > z and x+z > y and y+z > x):
    if (x == y and x == z):
        print('Esse triângulo é eqüilátero.')
    elif (x==y or x==z or y==z):
        print('Esse triângulo é isósceles')
    elif(x != y and x != z and y != z):
        print('Esse triângulo é escaleno')
else:
    print('Isso não é um triângulo')