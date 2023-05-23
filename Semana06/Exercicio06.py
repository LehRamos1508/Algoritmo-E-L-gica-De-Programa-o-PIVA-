acertos = int(input('Digite o número de questões corretas: '))

if acertos <= 49:
    print('Seu conceito é D')
elif acertos >= 50 and acertos <= 69:
    print('Seu conceito é C')
elif acertos >= 70 and acertos <= 80:
    print('Seu conceito é B')
elif acertos >= 90 and acertos <=100:
    print('Seu conceito é A')
else:
    print('''Não foi possível encontrar seu conceito na tabela
favor procurar seu professor afim de esclarecer dúvidas!!!''')

#Caro professor Piva, reiterando aqui que há uma lacuna na planilha na pontuação >80 e <90
#Não sabendo se é proposital ou não, fiz o programa levando isso em conta. Grato!
