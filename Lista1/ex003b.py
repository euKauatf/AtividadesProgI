# Exercício 3B: Escreva um programa que recebe três inteiros como entrada do teclado e escreva na tela a média, a soma, o produto, o menor valor e o maior valor, usando uma linha para cada resultado.
#
# Recebe 3 inteiros n1 n2 n3
#
# Calcula média = (n1 + n2 + n3) / 3
# Calcula soma = n1 + n2 + n3
# Calcula produto = n1 * n2 * n3
#
# Se n1 < n2
    # n1, n2 = n2, n1
# Se n1 < n3
    # n1, n3 = n3, n1
# Se n2 < n3
    # n2, n3 = n3, n2
#
# menor = n3
# maior = n1
#
# Imprime um em resultado em cada linha

# Recebe 3 inteiros n1 n2 n3
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

# Calcula os resultados
media = (n1 + n2 + n3) / 3
soma = n1 + n2 + n3
produto = n1 * n2 * n3

# Ordena os números para encontrar o menor e o maior
if (n1 < n2):
    n1, n2 = n2, n1
if (n1 < n3):
    n1, n3 = n3, n1
if (n2 < n3):
    n2, n3 = n3, n2

# Define menor e maior
menor = n3
maior = n1

# Imprime os resultados
print(f"Média: {media}")
print(f"Soma: {soma}")
print(f"Produto: {produto}")
print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")