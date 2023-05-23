nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+nota2)/2

if (media >= 5):
    print(f'Parabéns! Sua média foi {media} e você está aprovado!')
else:
    print(f'Infelizmente você está reprovado sua média foi {media}. Eu lhe aconselho a assistir o curso do Piva!')
