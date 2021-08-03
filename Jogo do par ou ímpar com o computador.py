'''Jogo do par ou ímpar com o computador.
O jogo é interrompido quando o jogador perder
O programa mostra o total de vitórias consecutivas que o usuário conquistou no final do jogo.'''

from random import randint
vitorias = 0
while True:
    computador = randint(0,10)
    jogador = int(input("Digite um valor: "))
    opcao = str(input("Par ou ímpar? [P/I] ")).upper()
    soma = computador + jogador
    if soma % 2 == 0:
        tipo = 'P'
    else:
        tipo = 'I'

    print(f"O valor é {soma}, o computador informou {computador} e você {jogador}")
    if opcao != tipo:
        print("Você perdeu")
        break
    else:
        print("Você ganhou")
        vitorias += 1
print(f"Você venceu {vitorias} partida(s)")