ano_nasc = int(input('Digite o ano em que você nasceu: '))
ano_atual = int(input('Digite o ano atual: '))
idade_anos = ano_atual-ano_nasc
idade_meses = idade_anos*12
idade_dias = idade_meses*30
idade_semana = idade_dias/7
print('Sua idade em anos é de {} anos'.format(idade_anos))
print('Sua idade em meses é de {} meses'.format(idade_meses))
print('Sua idade em dias é de {} dias'.format(idade_dias))
print('Sua idade em semanas é de {:.2f} semanas'.format(idade_semana))