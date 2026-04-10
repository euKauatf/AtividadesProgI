# Faça um jogo de pedra, papel, tesoura, spock e lagarto (de onde vem isso?), onde o jogador e o computador escolhem entre “0-pedra 1-spock 2-paper 3-lagarto 4-tesoura” (a jogado do computador é aleatória). Ganha o jogo quem vencer 3 vezes primeiro (As regras de vitória estão descritas na figura abaixo).

# Importa random
# pedra = 0
# spock = 1
# papel = 2
# lagarto = 3
# tesoura = 4
#
# acertosJ = 0
# acertosC = 0
#
# Enquanto (acertosJ != 3) e (acertosC != 3)
#   Recebe jogador
#   computador = random.randint(0, 4)
#
#   Se (jogador == computador)
#       empate
#   Senão se (jogador == pedra) e (computador == tesoura ou computador == lagarto)
#       jogador ganha
#       acertosJ++
#   Senão se (jogador == spock) e (computador == pedra ou computador == tesoura)
#       jogador ganha
#       acertosJ++
#   Senão se (jogador == papel) e (computador == spock ou computador == pedra)
#       jogador ganha
#       acertosJ++
#   Senão se (jogador == lagarto) e (computador == spock ou computador == papel)
#       jogador ganha
#       acertosJ++
#   Senão se (jogador == tesoura) e (computador == papel ou computador == lagarto)
#       jogador ganha
#       acertosJ++
#   Senão
#       computador ganha
#       acertosC++
# Imprime o resultado do jogo

# Instanciando variáveis
import random
pedra = 0
spock = 1
papel = 2
lagarto = 3
tesoura = 4

acertosJ = 0
acertosC = 0

while (acertosJ != 3) and (acertosC != 3): # Loop para decidir o vencedor
    jogador = int(input("Digite sua mão:\n0-pedra\n1-spock\n2-paper\n3-lagarto\n4-tesoura\n"))
    computador = random.randint(0, 4) # Escolha da mão do computador
    if computador == 0:
        computadorJogada = "pedra"
    elif computador == 1:
        computadorJogada = "spock"
    elif computador == 2:
        computadorJogada = "papel"
    elif computador == 3:
        computadorJogada = "lagarto"
    else:
        computadorJogada = "tesoura"
    
    # Condições de vitória, empate ou derrota
    if (jogador == computador):
        print(f"\nEmpate! O computador também jogou {computadorJogada}. Jogue novamente")
    elif (jogador == pedra) and (computador == tesoura or computador == lagarto):
        print(f"\nVocê ganhou essa rodada! O computador jogou {computadorJogada}")
        acertosJ += 1
    elif (jogador == spock) and (computador == pedra or computador == tesoura):
        print(f"\nVocê ganhou essa rodada! O computador jogou {computadorJogada}")
        acertosJ += 1
    elif (jogador == papel) and (computador == spock or computador == pedra):
        print(f"\nVocê ganhou essa rodada! O computador jogou {computadorJogada}")
        acertosJ += 1
    elif (jogador == lagarto) and (computador == spock or computador == papel):
        print(f"\nVocê ganhou essa rodada! O computador jogou {computadorJogada}")
        acertosJ += 1
    elif (jogador == tesoura) and (computador == papel or computador == lagarto):
        print(f"\nVocê ganhou essa rodada! O computador jogou {computadorJogada}")
        acertosJ += 1
    else:
        print(f"\nO computador ganhou essa rodada! O computador jogou {computadorJogada}")
        acertosC += 1

if (acertosJ == 3):
    print(f"\n\nVocê ganhou o jogo de {acertosJ} a {acertosC}!")
else:
    print(f"\n\nO computador ganhou o jogo de {acertosC} a {acertosJ}!")