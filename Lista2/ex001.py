#1) Interpretar e traduzir para Python a sequência de comandos em Português a seguir:
# Algoritmo {escrita dos termos de Fibonacci menores que L}
# leia o valor L
# {Processamento dos dois primeiros termos}
# Atribua o valor 1 ao termo1
# se ele for menor do que L então
#   escreva-o
# fim se
# Atribua o valor 1 ao termo2
# se ele for menor do que L então
#   escreva-o
# fim se
# {Processamento dos termos restantes}
# enquanto novo termo1 mais termo2 for menor ou igual a L faça
#   Calcule o novo termo somando os 2 anteriores
#   escreva o termo
#   Atribua termo2 a termo1
#   Atribua termo a termo2
# fim enquanto
# Fim algoritmo.

L = int(input("Digite o valor L: ")) # ler valor L
termo1 = 1 # atribuir valor 1 a termo1

if termo1 < L: # se termo1 for menor que L
    print(termo1) # escreva termo1

termo2 = 1 # atribuir valor 1 a termo2

if termo2 < L: # se termo2 for menor que L
    print(termo2) # escreva termo2

while termo1 + termo2 <= L: # enquanto termo1 mais termo2 for menor ou igual a L
    termo = termo1 + termo2 # calculo do novo termo com os 2 de antes
    print(termo) # escreva o termo
    termo1 = termo2 # atribuir termo2 a termo1
    termo2 = termo # atribuir termo a termo2
