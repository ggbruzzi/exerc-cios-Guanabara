# progama que serve para adicionarmos valores com o metodo input em uma lista
from ferramentas import linhas
resp = ''
list = []
while resp != 'N' :
    n = int(input('Digite um valor : '))
    if n in list :
        print('Valor já está na lista !')
    else :
        print('Valor adicionado a lista')
        list.append(n)
    resp = str(input('Quer continuar ? (S/N) ' )).upper()
linhas()
print('Você digitous os valores {}'.format(list))

