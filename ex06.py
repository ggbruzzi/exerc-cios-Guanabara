# Esse progama serve para analisar dados de um grupo de pessoas e classifica-los .
soma = 0
maior = 0
menor = 10000
nomemaisvelho = ''
muienova = 0
n = int(input('Qual o número de pessoas que deseja analisar ? '))
for i in range(1,n + 1) :
    print('Dados da {}ª pessoa'.format(i))
    nome = str(input('Nome : ')).strip()
    idade = int(input('Idade : '))
    soma = soma + idade
    sexo = str(input('Sexo [M][F] : ')).strip()
    if idade > maior and sexo in 'Mm' :
        maior = idade
        nomemaisvelho = nome
    elif idade < 20 and sexo in 'Ff' :
        muienova = muienova + 1
media = soma / n
print('A média da idade do grupo é {}'.format(media))
print('O homem mais velho é o {} e ele tem {} anos'.format(nomemaisvelho,maior))
print('{} mulheres tem menos de 20 anos'.format(muienova))

