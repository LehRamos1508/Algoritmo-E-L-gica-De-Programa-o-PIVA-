from math import pi, pow

def volumeEsfera(raio):
    volume = (4 * pi * pow(raio, 3)) / 3
    return volume


raio = float(input('Digite o valor do raio de uma esfera: '))
print(f'Uma esfera com raio igual a {raio} tem um volume igual a {volumeEsfera(raio):.2f}!')