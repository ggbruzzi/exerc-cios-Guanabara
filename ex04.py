# esse progama calcula uma PA de 10 termos
def main() :
    global p
    global r
    global decimo
    p = int(input('Digite o primeiro termo: '))
    r = int(input('Digite a razão: '))
    decimo = p + (9 * r)
    calcula_PA()



def calcula_PA() :
    for c in range (p,decimo + r,r) :
        print(c, end=' ' )
    print('ACABOU')



main()
