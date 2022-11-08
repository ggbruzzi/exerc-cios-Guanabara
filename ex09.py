# O progama serve para simular o sistema de uma loja .
from ferramentas import linhas
linhas()
print('Loja')
linhas()
menor = 100000000000000000000000
barato = ''
total = 0
while True :
    nome = str(input('Nome do produto : '))
    preco = float(input('Preço do produto : R$ '))
    total = total + preco
    if preco < menor :
        menor = preco
        barato = nome
    teste = str(input('Algo a mais ? [S/N] ')).strip().upper()[0]
    if teste in 'N' :
        break
    linhas()
print('O total da compra foi R${:.2f}'.format(total))
print('O produto mais barato foi {} custando {}'.format(barato,menor))

