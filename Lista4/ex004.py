'''4) Faça um programa que recebe uma lista de números inteiros de tamanho 100. O programa deve percorrer esta lista e imprimir na tela o valor mais próximo da média dos valores deste vetor.'''

# Cria uma lista para armazenar os números
#
# Para cada i de 1 a 100
#   Recebe um número do usuário
#   Adiciona o número à lista
# Calcula a média dos valores na lista
#
# Inicializa uma variável para armazenar o valor mais próximo da média
# Para cada número na lista
#   Se o número for mais próximo da média do que o valor armazenado
#       Atualiza o valor mais próximo da média



# Criando uma lista para armazenar os números inteiros
numeros = []

# Recebendo os 100 números inteiros do usuário
for i in range(100):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)

# Calculando a média dos valores na lista
media = sum(numeros) / len(numeros)

# Inicializando uma variável para armazenar o valor mais próximo da média
valorMaisProximo = numeros[0]
for numero in numeros:
    if abs(numero - media) < abs(valorMaisProximo - media):
        valorMaisProximo = numero

# Imprimindo o valor mais próximo da média
print(f"O valor mais próximo da média ({media}) é: {valorMaisProximo}")