import random
from ferramentas import linhas
# esse progama pensa em um número de 0 a 10 e pede para o usuário ir tentando adivinhar


def main() :
    global computador
    global n
    n = 1
    computador = random.randint(0,10)
    linhas()
    print('Vou pensar em um número inteiro entre 0 e 10. Tente adivinhar para vencer')
    linhas()
    funcionamento()


def funcionamento():
    global n
    escolha = int(input('Qual número eu pensei ? '))
    while escolha != computador :
        escolha = int(input('Ainda não acertou... tente novamente : '))
        n = n + 1
    print('Você acertou ! E precisou de {} tentativas'.format(n))


main()