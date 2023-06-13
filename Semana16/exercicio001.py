lista = []
    
def pegarSobrenome() :
    while True:
        sobrenome = input('Digite o sobrenome: ')
        if sobrenome:
            if sobrenome.isalpha():
                return sobrenome
            else:
                print('Digite um sobrenome válido!')
        else:
            return sobrenome

def pegarIdade():
    while True:
        try:
            idade = int(input('Digite uma idade: '))
        except:
            print('Digite uma idade válida')
        else:
            if idade:
                return idade
            else:
                print('Digite uma idade válida')

def pegarAltura ():
    while True:
        try:
            altura = int(input('Digite uma altura (cm): '))
        except:
            print('Digite uma altura válida')
        else:
            if altura:
                return altura
            else:
                print('Digite uma altura válida')

def pegarPeso():
    while True:
        try:
            peso = float(input('Digite um peso (Kg): '))
        except:
            print('Digite um peso válido')
        else:
            if peso:
                return peso
            else:
                print('Digite um peso válido')

def valoresNaLista (sobrenome, idade, altura, peso):
    pessoa = []
    pessoa.append(sobrenome)
    pessoa.append(idade)
    pessoa.append(altura)
    pessoa.append(peso)

    lista.append(pessoa)

n = 0
while True:
        sobrenome = pegarSobrenome()
        if sobrenome:
            n += 1
            idade = pegarIdade()
            altura = pegarAltura()
            peso = pegarPeso()
            valoresNaLista(sobrenome, idade, altura, peso)
        else:
            break

if n > 1:
    lista.sort()

    somaIdade = 0 
    somaAltura= 0 
    somaPeso = 0 
    
    print("-------------------------------------------------")
    for i in range(0, len(lista)):
        print(f"{lista[i][0]:10} - {lista[i][1]} - {lista[i][2]} - {lista[i][3]:5.1f}")
        somaIdade += lista[i][1]
        somaAltura += lista[i][2]
        somaPeso += lista[i][3]
    print("-------------------------------------------------")

    mediaIdade = somaIdade / n
    mediaAltura = somaAltura / n
    mediaPeso = somaPeso / n
    print(f"Idade média: {mediaIdade}")
    print(f"Altura média: {mediaAltura}")
    print(f"Peso médio: {mediaPeso}")
    print("-------------------------------------------------")