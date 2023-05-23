nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
media1= (nota1 + nota2 + nota3) / 3
notaexame = 12 - media1

if (media1 >= 0 and media1 <3):
    print(f'Sua média foi {media1:.1f}. Infelizmente você foi reprovado')
elif (media1 >=3 and media1 <7):
    print(f'Sua média foi {media1:.1f}. Você precisará fazer o exame.')
    print(f'Para ser aprovado você precisa tirar ao menos {notaexame:.1f} no exame')
else:
    print(f'Sua média foi {media1:.1f}. Parabéns, você foi aprovado!')