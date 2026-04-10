# determinar todos os números de 3 algarismos, cujas somas dos cubos dos algarismos sejam iguais ao próprio número. Exemplo: 153 = 1**3 + 5**3 + 3**3.

# laço for de i a 999
#    Se (algarismo1**3 + algarismo2**3 + algarismo3**3) == i
#        Imprime i

# Laço for de i a 999
for i in range(100, 1000):
    # Se (algarismo1**3 + algarismo2**3 + algarismo3**3) == i
    algarismo1 = i // 100 # Pega a centena
    algarismo2 = (i // 10) % 10 # Pega o algarismo dezena
    algarismo3 = i % 10 # Pega o da unidade

    if (algarismo1 ** 3 + algarismo2 ** 3 + algarismo3 ** 3) == i: # Se a soma dos cubos dos alg for igual ao número
        print(i) # Imprime i