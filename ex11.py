# Lê o nome e a média de um aluno em um dict , armazenando e mostrando na tela
def main() :
    global aluno
    n = int(input('Quantos alunos serão analisados ? '))
    for c in range(0,n) :
        aluno = dict()
        aluno['Nome'] = str(input('Nome do aluno : '))
        verifica_media()
        print(aluno)


def verifica_media() :
    aluno['Media'] = 0
    while True :
        aluno['Media'] = float(input('Média do aluno(0 a 10) : '))
        if aluno['Media'] >= 0 and aluno['Media'] <= 10 :
            break
    return aluno['Media']

main()





