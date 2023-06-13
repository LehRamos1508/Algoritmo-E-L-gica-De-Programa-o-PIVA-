dic = {}

for _ in range(3):
    sobrenome = input('Digite o seu sobrenome: ')
    idade = int(input('Digite a sua idade: '))
    dic[sobrenome] = idade

arrayIdades = []
for i in dic.values():
    arrayIdades.append(i)

maiorIdade = max(arrayIdades)
for x, y in dic.items():
    if y == maiorIdade:
      print(f'O sobrenome da pessoa com a maior idade é {x}, e sua idade é {y} anos!')
      break