# gerar os cinquenta primeiros termos da série: 1 + N, 5 * N, 9 + N, 13 * N, ..., onde N é um valor lido.

# Recebe o valor de N
# laço for de i a 50
#    Se i for par
#        Imprime ((4*i+1) + N)
#    Se i for ímpar
#        Imprime ((4*i+1) * N)

# Recebe o valor de N
N = int(input("Digite um valor inteiro para N: "))

# Laço for de i a 50
for i in range(50):
    if i % 2 == 0: # Se i for par
        print((4 * i + 1) + N) # Imprime ( (4*i+1) + N)
    else: # Se i for ímpar
        print((4 * i + 1) * N) # Imprime ( (4*i+1) * N)