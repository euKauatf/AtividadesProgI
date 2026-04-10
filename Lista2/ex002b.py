# Faça um programa para construir a tabela de multiplicação de números de 1 a 10 (ex.: 1 x 1 = 1, 1 x 2 = 2, ....,2 x 1 = 2, 2 x 2 = 4, ...., etc.).

# laço for de i a 10
#    laço for de j a 10
#        Imprime i x j = i*j

# Laço for de i a 10
for i in range(1, 11):
    # Laço for de j a 10
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}") # Imprime i x j = i*j