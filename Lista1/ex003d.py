# Escreva um programa que recebe três números e retorna a soma deles, porém se houver números repetidos o valor deles não é contabilizado. Por exemplo, na entrada (1,2,3) a resposta é 6, na entrada (3,2,3) a resposta é 2 e na entrada (3,3,3) a resposta é 0.
#
# Recebe 3 números n1, n2, n3
#
# Se n1 == n2 == n3
    # Imprime 0
# Senão se n1 == n2
    # Imprime n3
# Senão se n2 == n3
    # Imprime n1
# Senão se n1 == n3
    # Imprime n2
# Senão
    # Imprime a soma de todos os números


# Recebe 3 números n1, n2, n3
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

# Verifica as condições para calcular a soma (Se não tiver números repetidos)
if (n1 == n2 and n1 == n3): # Todos os números repetidos imprimirão 0
    print("0")
elif (n1 == n2):
    print(f"{n3}")
elif (n2 == n3):
    print(f"{n1}")
elif (n1 == n3):
    print(f"{n2}")
else: # Nenhum número repetido (Soma)
    print(f"{n1 + n2 + n3}")