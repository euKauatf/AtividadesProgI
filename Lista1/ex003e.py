# Exercício 3e: Escreva um programa que receba três números. O programa deve imprimir a palavra “soma” se a soma de dois deles for igual ao outro número, caso contrário, o programa deve imprimir a palavra “multi” se a multiplicação de dois deles for igual ao outro número. Caso nenhuma das duas possibilidades for verdade, então imprimir a palavra “par” se a soma dos três números for par, e imprimir a palavra “impar” caso contrário. Por exemplo, na entrada (8,3,5) a resposta é “soma”, na entrada (3,3,1) a resposta é “multi”, na entrada (8,4,9) a resposta é “impar”.
#
# Recebe 3 números n1, n2, n3
#
# Se n1 + n2 == n3 ou n1 + n3 == n2 ou n2 + n3 == n1
    # Imprime "soma"
# Senão se n1 * n2 == n3 ou n1 * n3 == n2 ou n2 * n3 == n1
    # Imprime "multi"
# Senão se (n1 + n2 + n3) % 2 == 0
    # Imprime "par"
# Senão
    # Imprime "impar"


# Recebe 3 números n1, n2, n3
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if (n1 + n2 == n3) or (n1 + n3 == n2) or (n2 + n3 == n1): # Se a soma de dois números for igual ao outro, imprime "soma"
    print("soma")
elif (n1 * n2 == n3) or (n1 * n3 == n2) or (n2 * n3 == n1): # Se a multiplicação de dois números for igual ao outro, imprime "multi"
    print("multi")
elif (n1 + n2 + n3) % 2 == 0: # Se a soma dos três números for par, imprime "par"
    print("par")
else: # Se nenhuma das condições anteriores for verdadeira, é porque a soma é ímpar, então imprime "impar"
    print("impar")