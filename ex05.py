# O progama abaixo serve para indificar se um número é primo
def main() :
    global n
    global div
    n = int(input('Digite um número: '))
    div = 0
    verifica_numero()


def verifica_numero() :
    global div
    for c in range(1,n+1):
        if n % c == 0:
            print('o número {} é divísivel por {}'.format(n, c))
            div = div + 1
    if div == 2 :
        print ('O número {} é primo'.format(n))
    else :
        print('O número {} não é primo'.format(n))



main()
