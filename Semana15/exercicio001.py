def cabecalhoRelatorio ():
    text = 'ACME Inc.                              Uso do espaço em disco pelos usuários\n' + ('-'*76) + '\n' + 'Nr.    Usuário                 Espaço Utilizado              "%" do uso\n'
    return text

def criarLinhas(lista, soma):
    cont = 1
    linha = ''
    for i in lista:
        numero = i['numeroMB']
        porcentagem = numero * 100 / soma
        numero, porcentagem = f'{numero:.2f}', f'{porcentagem:.2f}'
        nome = i['nomeUsuario']
        linha += f'{cont}      {nome:<9}                   {numero:>7}MB                   {porcentagem:>5}%\n'
        cont += 1
    
    return linha

def rodapeRelatorio(soma, media):
    textoRodape = f'\nEspaço total armazenado = {soma:.2f}MB\nEspaço Médio Ocupado = {media:.2f}MB'
    return textoRodape

def converterMB (bytes):
    bytes = int(bytes)
    return (bytes / 1048576)
    

arquivoUsuarios = open('usuarios.txt', encoding='utf-8')

texto = arquivoUsuarios.read()
listaUsuarios = texto.split('\n')

lista = []
for i in listaUsuarios:
    user = i.split(',')
    lista.append(user)

arquivoUsuarios.close()

# # ==============================================================

arquivoRelatorio = open('relatorio.txt', 'w', encoding='utf-8')
cabecalho = cabecalhoRelatorio()

somaMB = 0
listaUsusariosENumeros = []
for y in lista:
    nomeUsuario = y[0]
    numeroMB = converterMB(y[1])
    listaUsusariosENumeros.append({'nomeUsuario': nomeUsuario, 'numeroMB': numeroMB})
    somaMB += numeroMB

media = somaMB / 6

textoConteudoPrincipal = criarLinhas(listaUsusariosENumeros, somaMB)

rodape = rodapeRelatorio(somaMB, media)
    
arquivoRelatorio.write(cabecalho)
arquivoRelatorio.write(textoConteudoPrincipal)
arquivoRelatorio.write(rodape)

arquivoRelatorio.close()