'''5) Faça um programa que receba duas listas, uma de tamanho N e outra de tamanho M. O programa deve percorrer as duas listas e intercalar os elementos de ambas, formando uma terceira lista. A terceira lista deve começar pelo primeiro elemento da lista menor. Quando acabar de intercalar os elementos, se ainda tiver elementos sobrando na lista maior, colocar esses elementos no fim da terceira lista.'''

# Cria duas listas para armazenar os elementos
#
# Recebe a dimensão N da primeira lista
# Para cada i de 1 a N
#   Recebe um valor e adicionar à primeira lista
#
# Recebe a dimensão M da segunda lista
# Para cada i de 1 a M
#   Recebe um valor e adicionar à segunda lista
#
# Cria uma terceira lista para armazenar os elementos intercalados
# Para cada i de 0 até o tamanho da menor lista
#   Adiciona o elemento da primeira lista à terceira lista
#   Adiciona o elemento da segunda lista à terceira lista
#
# Se a primeira lista for maior que a segunda
#   Adiciona os elementos restantes da primeira lista à terceira lista
# Senão
#   Adiciona os elementos restantes da segunda lista à terceira lista



# Criando as duas listas para armazenar os elementos
lista1 = []
lista2 = []

# Recebendo a dimensão N da primeira lista
N = int(input("Digite a dimensão N da primeira lista: "))
# Recebendo os elementos da primeira lista do usuário
for i in range(N):
    valor = input(f"Digite o {i+1}º elemento da primeira lista: ")
    lista1.append(valor)

# Recebendo a dimensão M da segunda lista
M = int(input("Digite a dimensão M da segunda lista: "))
# Recebendo os elementos da segunda lista do usuário
for i in range(M):
    valor = input(f"Digite o {i+1}º elemento da segunda lista: ")
    lista2.append(valor)

# Criando a terceira lista para armazenar os elementos intercalados
listaIntercalada = []
# Intercalando os elementos das duas listas
for i in range(min(N, M)):
    listaIntercalada.append(lista1[i])
    listaIntercalada.append(lista2[i])

# Adicionando os elementos restantes da lista maior à terceira lista
if N > M:
    listaIntercalada.extend(lista1[M:])
else:
    listaIntercalada.extend(lista2[N:])

# Imprimindo a terceira lista intercalada
print("Lista intercalada:", listaIntercalada)