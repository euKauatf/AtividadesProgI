# Exercício 3f: Faça um programa que leia três coordenadas num espaço 2D e indique se formam um triângulo, juntamente com o seu tipo (equilátero, isósceles e escaleno):
#i. Equilátero: todos os lados iguais
#ii. Isósceles: dois lados iguais
#iii. Escaleno: todos os lados diferentes
#Condição de existência) um triângulo com lados de tamanho a,b,c existe se :
#| b - c | < a < b + c
#| a - c | < b < a + c
#| a - b | < c < a + b
#
# Recebe os lados A B e C
#
# Se os lados formam um triângulo
#    # Imprime "Formam um triângulo, do tipo: "
#
#    Se A == B == C
#        Imprime "Triângulo Equilátero"
#    Senão se A == B ou A == C ou B == C
#        Imprime "Triângulo Isósceles"
#    Senão
#        Imprime "Triângulo Escaleno"

# Recebe os lados A B e C
A = int(input("Digite o lado A: "))
B = int(input("Digite o lado B: "))
C = int(input("Digite o lado C: "))

# Condição de existência do triângulo
if (abs(B - C) < A < (B + C)) and (abs(A - C) < B < (A + C)) and (abs(A - B) < C < (A + B)):
    print("Formam um triângulo, do tipo: ")

    # Verifica o tipo do triângulo
    if A == B == C:
        print("Triângulo Equilátero")
    elif A == B or A == C or B == C:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")