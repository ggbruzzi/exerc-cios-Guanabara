# progama que serve para analisar a idade e alistamento obrigatório

def main() :
     global ano
     global idade
     global completar
     global jatem
     ano = int(input('Ano de nascimento : '))
     idade = 2022 - ano
     completar = 18 - idade
     jatem = idade - 18
     verificaIdade()



def verificaIdade() :
    if idade == 18:
        print('Quem nasceu em {} completa 18 anos esse ano e deve alistar imediatamente'.format( ano))
    elif idade < 18 :
        print('Quem nasceu em {} ainda tem {} anos e não pode se alistar.Você vai completar 18 anos daqui a {} anos'.format( ano, idade, completar))
    else :
     print('Quem nasceu em {}, tem {} anos e já deveria ter se alistado a {} anos atrás. Vá IMEDIATAMENTE'.format( ano, idade, jatem))



main()
