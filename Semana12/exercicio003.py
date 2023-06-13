def anoBissexto (ano):
    if ((ano % 4 == 0) and (ano % 100 != 0)):
        return print(f'{ano} É BISSEXTO!')
    elif ((ano % 4 == 0) and (ano % 100 == 0) and (ano % 400 == 0)):
        return print(f'{ano} É BISSEXTO!') 
    else:
        return print(f'{ano} NÃO É BISSEXTO!')
      
       
                

while True:
    ano = int(input('Digite um ano para verificar se é bissexto: '))
    if ano == 0:
      break
    anoBissexto(ano)