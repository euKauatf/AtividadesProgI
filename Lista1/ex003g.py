# Faça um programa que a partir de um número informado em centavos (inteiro), indique a menor quantidade de moedas que representa esse valor. Considere moedas de 1,25 e 50 centavos e 1 real (100 centavos). Exemplo: 290 centavos é representado por 2 moedas de 1 real, 1 de 50c, 1 de 25c, 15 de 1c.
#
# Recebe o valor em centavos
# Se o valor for maior ou igual a 100
#    Imprime a quantidade de moedas de 1 real (valor // 100)
#    Atualiza o valor (valor % 100)
# Se o valor for maior ou igual a 50
#    Imprime a quantidade de moedas de 50 centavos (valor // 50)
#    Atualiza o valor (valor % 50)
# Se o valor for maior ou igual a 25
#    Imprime a quantidade de moedas de 25 centavos (valor // 25)
#    Atualiza o valor (valor % 25)
# Imprime a quantidade de moedas de 1 centavo (valor)

# Recebe o valor em centavos
centavos = int(input("Digite o valor em centavos: "))

# Condições para cada uma das moedas
if centavos >= 100: # Um real
    print(f"Moedas de 1 real: {centavos // 100}")
    centavos = centavos % 100
if centavos >= 50: # Cinquenta centavos
    print(f"Moedas de 50 centavos: {centavos // 50}")
    centavos = centavos % 50
if centavos >= 25: # Vinte e cinco centavos
    print(f"Moedas de 25 centavos: {centavos // 25}")
    centavos = centavos % 25
if centavos >= 1: # Um centavo
    print(f"Moedas de 1 centavo: {centavos}") # O que sobrou vai ser a quantidade de moedas de 1 centavo