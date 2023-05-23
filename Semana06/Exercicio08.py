import math
pe_direito = 2.8
porta = 0.8 * 2.10
largura = float(input('Digite a largura do aposento em metros (00.00) : '))
comprimento = float(input('Digite o comprimento do aposento em metros (00.00) : '))
lata_tinta = float(input('Digite o tamanho da lata de tinta em litros: '))
area_aposento = (((largura + comprimento) *2) * pe_direito) - porta
rendimento_Litro_Tinta = area_aposento / 3
latas_necessarias = rendimento_Litro_Tinta / lata_tinta
latas_necessarias = math.ceil(latas_necessarias)

print(f'Para pintar esse aposento você vai precisar de {latas_necessarias} latas de tinta')