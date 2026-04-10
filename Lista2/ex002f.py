# Escreva um programa que imprime na tela os n primeiros números perfeitos. Um número perfeito é aquele que é igual à soma dos seus divisores (tirando ele mesmo). Por exemplo, 6 = 1 + 2 + 3 é perfeito.

# Recebe um número n
# perfeitos = 0
# i = 1
# Laço while enquanto nao tiver encontrado n perfeitos
#    soma = 0
#    Laço for de j a i-1
#        Se i % j == 0
#            soma += j
#    i += 1
#    Se soma == i
#        Imprime i é perfeito

# Recebe um número n
n = int(input("Digite a quantidade de números perfeitos que deseja imprimir: "))
perfeitos = 0 # Contador de números perfeitos encontrados

i = 1 # Começa a verificar a partir do número 1

while perfeitos < n:
    soma = 0 # Soma dos divisores
    for j in range(1, i): # Laço for de j a i-1
        if i % j == 0: # Caso j seja divisor de i
            soma += j

    if soma == i: # Se a soma dos divisores for igual a i
        print(f"{i} é perfeito.") # Imprime que i é perfeito
        perfeitos += 1 # Incrementa o contador de números perfeitos encontrados

    i += 1 # Incrementa i para verificar o próximo número