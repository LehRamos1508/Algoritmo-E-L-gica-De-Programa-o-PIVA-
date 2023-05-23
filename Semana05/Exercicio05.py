anoAtual = int(input('Digite o ano atual: '))
anoNasc = int(input('Digite o ano do seu nascimento: '))
idade = anoAtual - anoNasc

if (idade >= 16):
    if (idade <18):
        print(f'Você possui {idade} anos, com essa idade você já pode votar, mas ainda não pode tirar a carteira de habilitação.')
    else:
        print(f'Você possui {idade} anos, com essa idade você já pode votar e tirar sua carteira de habilitação.')
else:
    print(f'Você possui {idade} anos, com essa idade você ainda não pode votar ou tirar sua carteira de habilitação.')
