def conversao (horas, minutos, segundos):
    horas = int(horas)
    minutos = int(minutos)
    segundos = int(segundos)
    return (horas * 3600) + (minutos * 60) + segundos

horasMinutosSegundos = input('Digite as horas (h:m:s): ')
arrayHoras = horasMinutosSegundos.split(':')

print(f'{arrayHoras[0]} Horas, {arrayHoras[1]} Minutos e {arrayHoras[2]} Segundos valem {conversao(arrayHoras[0], arrayHoras[1], arrayHoras[2])} segundos!')
