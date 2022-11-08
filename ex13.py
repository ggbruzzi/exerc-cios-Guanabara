# Jogo da adivinhação contra o computador
import random
from time import sleep
computador = random.randint(0,5)
print('-=-' * 20)
print('Vou pensar em um número inteiro entre 0 e 5, tente adivinhar para vencer')
print('-=-' * 20)
num = int(input('Qual número eu pensei (0-5)? '))
print('PROCESSANDO...')
sleep(3)
if num == computador :
    print('Parabéns ! você venceu!')
else :
    print('Que pena ! você perdeu... eu pensei no número {}'.format(computador))