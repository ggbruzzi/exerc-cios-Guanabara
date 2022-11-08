# O progama serve para o cadastro de jogadores e quantos gols cada um fez.
while True :
    jogador = dict()
    partidas = list()
    jogador['nome'] = str(input('Nome do jogador : '))
    n = int(input(f'Quantas partidas o {jogador["nome"]} jogou ? '))
    for c in range(1,n + 1) :
        partidas.append(int(input(f'Quantos gols na partida {c} ? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    print(jogador)
    decisao = str(input('Quer continuar[S/N] ? ')).strip().upper()
    if decisao == 'N' :
        break