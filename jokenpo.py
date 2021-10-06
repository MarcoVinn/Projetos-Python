from random import randint
x = int(input('[0] Pedra \n[1] Papel \n[2] Tesoura: \n'))
bot = randint(0, 1)
ppt = {0: 'Pedra',
       1: 'Papel',
       2: 'Tesoura'}
if x == bot:
    print({ppt[bot]}, 'Empate')
elif x == 0 and bot != 1:
    print('A maquina tirou ', ppt[bot], ' Voce Ganhou')
elif x == 1 and bot != 2:
    print('A maquina tirou ', ppt[bot], ' Voce Ganhou')
elif x == 2 and bot != 0:
    print('A maquina tirou ', ppt[bot], ' Voce Ganhou')
else:
    print('A maquina tirou ', ppt[bot], ' Voce Perdeu')
