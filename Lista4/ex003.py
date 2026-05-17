'''3) Faça um programa que receba uma lista A de dimensão N e:
(a) Inverta os valores de A, troque o primeiro pelo ultimo, o segundo pelo penúltimo e assim por diante.
(b) Após este procedimento, criar um vetor B de dimensão N com o fatorial de cada valor de A, respeitando as posições, caso o valor for positivo ou nulo. Deixe os valores negativos intactos.
(c) Imprima o vetor B.'''

# Cria uma lista A
# Recebe a dimensão N da lista A
# Para cada i de 1 a N
#   Recebe um valor e adicionar à lista A
#
# Inverte os valores de A
#
# Cria uma lista B
# Para cada valor em A invertida
#   Se o valor for positivo ou nulo
#       Calcula o fatorial do valor e adiciona à lista B
#   Senão
#       Adiciona o valor negativo à lista B
# Imprime o vetor B



# Função para calcular o fatorial de um número
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

# Criando uma lista para armazenar os elementos de A
A = []
# Recebendo a dimensão N da lista A
N = int(input("Digite a dimensão N da lista A: "))

# Recebendo os elementos de A do usuário
for i in range(N):
    valor = int(input(f"Digite o {i+1}º elemento de A: "))
    A.append(valor)
# Invertendo os valores de A
AInvertida = A[::-1]

# Criando a lista B para armazenar os resultados do fatorial
B = []
for valor in AInvertida:
    if valor >= 0:
        B.append(fatorial(valor))
    else:
        B.append(valor)

# Imprimindo o vetor B
print("Vetor B:", B)