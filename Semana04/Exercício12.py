altura_Degrau = float(input('Digite a altura do degrau em centímetros: '))
altura_subida = float(input('Digite em metros a altura que deseja subir: '))
objetivo = (altura_subida*100)/altura_Degrau

print('Para chegar ao seu objetivo você precisará subir {} degraus'.format(objetivo))