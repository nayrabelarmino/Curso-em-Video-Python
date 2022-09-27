from random import randint
from time import sleep
computador = randint(0, 5)  #FAZ O COMPUTADOR "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
num = int(input('Em que número eu pensei? '))  #JOGADOR TENTA ADIVINHAR!
print('PROCESSANDO...')
sleep(3)
if num == computador:
    print('GANHOU! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, num))

