from exercicio002_funcao import aleatoryNumber
from time import sleep

contPlayer = 0
contComputer = 0
while True:
    print(f'\nJOGADOR {contPlayer} X {contComputer} COMPUTADOR')
    playOrNot = input('\nDeseja iniciar o jogo lançando o dado (s/n): ')
    if playOrNot == 'n':
        print('\nsaindo da aplicação...')
        break
    else:
        print('Jogador Lançando o dado!')
        sleep(1)
        playerNumber = aleatoryNumber()
        print(f'\nJogador... Número: {playerNumber}')
        computerNumber = aleatoryNumber()
        print('\nVez do computador lançar o dado!')
        sleep(1)
        print(f'Computador... Número: {computerNumber}')
        if playerNumber > computerNumber:
            contPlayer += 1
            print('\nJogador ganhou!!!')
        elif computerNumber > playerNumber:
            contComputer += 1
            print('\nComputador ganhou!')
        else:
            print('\nRodada terminou em empate!')

