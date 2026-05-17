'''1) Faça um programa em Python que receba um conjunto de 100 elementos numéricos e os armazene em uma lista. Em seguida, o programa deverá procurar se existem no vetor elementos iguais a um dado valor também informado pelo usuário e imprimir o índice das posições em que estes são encontrados.'''

# Cria uma lista para armazenar
#
# Para cada i ate 100
#   Recebe um numero do usuario
#   Adiciona o numero a lista
#
# Recebe o valor a ser procurado
# Para cada numero na lista
#   Se o numero for igual ao valor procurado
#       Adiciona o indice do numero a uma lista de indices encontrados
#
# Se a lista de indices encontrados não estiver vazia
#   Imprime os indices encontrados
# Senão
#   Imprime que não foram encontrados elementos iguais ao valor procurado


# Criando uma lista para armazenar os elementos
numeros = []

# Recebendo os 100 elementos numéricos do usuário
for i in range(100):
    numero = float(input(f"Digite o {i+1}º elemento numérico: "))
    numeros.append(numero)

# Recebendo o valor a ser procurado
valorProcurado = float(input("Digite o valor a ser procurado: "))

# Procurando por elementos iguais ao valor informado
indicesEncontrados = []
for i, numero in enumerate(numeros):
    if numero == valorProcurado:
        indicesEncontrados.append(i)

# Imprimindo os índices das posições em que os elementos foram encontrados
if indicesEncontrados:
    print(f"Elementos iguais a {valorProcurado} encontrados nas posições: {indicesEncontrados}")
else:
    print(f"Não foram encontrados elementos iguais a {valorProcurado}.")