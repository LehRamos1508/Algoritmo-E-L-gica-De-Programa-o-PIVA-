hora_real = float(input('Digite a hora no formato (hh.mm): '))

hora = int(hora_real)
minutos = float((hora_real - hora) * 100)

total_minutos = hora * 60 + minutos
print(f'A hora digitada em minutos é:{total_minutos}')
