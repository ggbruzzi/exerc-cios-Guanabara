# Esse progama nos mostra a tabuada do valor escolhido pelo usuário .
n = 0
c = 1
while n >= 0 :
    n = int(input('Quer ver a tabuada de qual valor ? '))
    if n < 0 :
        break
    while c <= 10 :
        print('{} x {} = {}'.format(n,c,n * c))
        c = c + 1
    c = 1
print('Fim do programa !')