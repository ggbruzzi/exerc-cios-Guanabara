# O progama serve para verificarmos a media de duas notas do aluno e ver se ele esta aprovado ou não
from ferramentas import media
def main() :
    global n1
    global n2
    while True :
        n1 = float(input('Primeira nota(0 a 10) : '))
        if n1 >= 0 and n1 <= 10 :
            break
    while True :
        n2 = float(input('Segunda nota(0 a 10) : '))
        if n2 >= 0 and n2 <= 10 :
            break
    print('Tirando {:.2f} e {:.2f} a média do aluno será {:.2f}'.format(n1,n2,media(n1,n2)))
    verifica_media()



def verifica_media() :
    if (media(n1,n2) > 6) :
        print('O aluno está APROVADO')
    elif (media(n1,n2) < 4) :
        print('O aluno está REPROVADO')
    else :
        print('O aluno está de RECUPERÇÃO')


main()
