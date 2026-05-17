'''2) Uma locadora de videogame tem guardada, em uma lista de 500 posições, a quantidade de jogos retirados por seus clientes durante o ano passado (i.e. Clientes[i] = X -> o cliente “i” retirou X jogos no ano passado). Agora esta locadora está fazendo uma promoção e, para cada 10 jogos retirados no ano passado, o cliente tem direito a uma locação grátis. Faça um programa que crie um outro vetor contendo a quantidade de locações gratuitas a que cada cliente tem direito.'''

# Cria uma lista de clientes
# Para cada cliente de 1 a 500
#   Recebe a quantidade de jogos retirados
#   Adiciona a quantidade de jogos à lista de clientes
#
# Cria uma lista de locações
# Para cada quantidade de jogos na lista de clientes
#   Calcula a quantidade de locações
#   Adiciona a quantidade de locações à lista de locações gratuitas
#
# Para cada cliente de 1 a 500
#   Imprime a quantidade de locações gratuitas que o cliente tem direito


# Criando uma lista para armazenar a quantidade de jogos retirados por cada cliente
clientes = []

# Recebendo a quantidade de jogos retirados por cada cliente
for i in range(500):
    jogosRetirados = int(input(f"Digite a quantidade de jogos retirados pelo cliente {i+1}: "))
    clientes.append(jogosRetirados)

# Criando uma lista para armazenar a quantidade de locações gratuitas a que cada cliente tem direito
locacoesGratis = []

# Calculando a quantidade de locações gratuitas para cada cliente
for jogos in clientes:
    locacoesGratis.append(jogos // 10)

# Imprimindo a quantidade de locações gratuitas para cada cliente
for i, locacoes in enumerate(locacoesGratis):
    print(f"Cliente {i+1} tem direito a {locacoes} locações gratuitas.")