# Suponha que um jogador A de PokemonGO tenha 800 pokemons com uma taxa de anual de crescimento/captura de 3% e que o jogador B tem 2000 pokemons com uma taxa de crescimento/captura de 1.5%. Faça um programa que calcule e retorne o número de anos necessários para que o jogador A ultrapasse ou iguale o número de pokemons do jogador B, mantidas as taxas de crescimento.

# crescA = 0.03, crescB = 0.015
# pokA = 800, pokB = 2000
# anos = 0
# Enquanto pokA <= pokB
#   pokA += pokA * crescA
#   pokB += pokB * crescB
#   anos += 1
# Imprime a quantidade de anos

# Instanciando variáveis
crescA = 0.03
crescB = 0.015
pokA = 800
pokB = 2000
anos = 0

# Laço while para que o jogador A seja maior ou igual a B com o decorrer dos anos
while pokA <= pokB:
    pokA += pokA * crescA # pokA += pokA * crescA
    pokB += pokB * crescB # pokB += pokB * crescB
    anos += 1 # anos += 1

print(f"Quantidade de anos necessários para que a quantidade de pokemons do jogador A ({pokA:.0f}) ultrapasse ou iguale a do jogador B ({pokB:.0f}): {anos}")