# Faça um programa que determina se dois valores inteiros e positivos A e B são “Bros” (dois números inteiros são ditos “Bros”, caso não exista divisor comum aos dois números diferente de 1).

# Recebe A e B
# dA = A
# dB = B
# bros = False
#
# Enquanto (dA%dB != 1) e (!bros)
#   Se (dA % dB == 0)
#       bros = True
#   Senão
#       aux = dA
#       dA = dB
#       dB = aux % dA
#
# Se (bros):
#   imprime são bros
# Senão
#   imprime não são bros

# Instanciando variáveis
A = int(input("Digite o valor de A:\n"))
B = int(input("Digite o valor de B:\n"))
dA = A
dB = B
bros = False

# Enquanto não forem bros ou o MDC ser diferente de 1
while (dA % dB != 1) and (not bros):
    if (dA % dB == 0): # Caso haja um MDC != 1
        bros = True
    else:
        aux = dA
        dA = dB # dA vai ser o dB anterior
        dB = aux % dA #dB vai ser o resto da divisão de dA anterior com dB anterior

if (bros):
    print(f"os números {A} e {B} são bros!")
else:
    print(f"os números {A} e {B} não são bros!")