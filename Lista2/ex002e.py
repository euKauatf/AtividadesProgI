# Um número inteiro é considerado triangular se este for o produto de 3 números inteiros consecutivos, como, por exemplo, 120 = 4 x 5 x 6. Elabore um programa que, após ler um número n do teclado, verifique se n é triangular.

# Recebe um número n
# Laço while de i a n enquanto nao for triangular
#    Se (i * (i+1) * (i+2)) == n
#        Imprime n é triangular

# Recebe um número n
n = int(input("Digite um número inteiro para verificar se é triangular: "))
triangular = False # Variável sentinela

# Laço while de i a n
i = 0
while i < n and not triangular: # Enquanto i for menor que n e não tiver encontrado um número triangular
    if (i * (i + 1) * (i + 2)) == n: # Se (i * (i+1) * (i+2)) == n
        print(f"{n} é triangular.") # É triangular
        triangular = True
    i += 1

if not triangular: # Se o laço terminou sem encontrar um número triangular
    print(f"{n} não é triangular.") # Imprime n não é triangular