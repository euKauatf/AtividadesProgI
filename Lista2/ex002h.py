# Fazer um programa que lê n números inteiros do teclado, e no final informa se os números lidos estão ou não em ordem crescente.

# Recebe N
# anterior = 0
# emOrdem = True
# i = 0
#
# while (emOrdem) and (i < N):
#    Recebe valor
#
#    Se i == 0
#        anterior = valor
#    Se valor < anterior
#        Imprime os números não estão em ordem crescente
#        emOrdem = False
#
#    anterior = valor
#    i += 1
#
# Se emOrdem
#    Imprime os números estão em ordem crescente

# Instanciando variáveis
N = int(input("Digite a quantidade de números inteiros que deseja inserir: "))
anterior = 0
emOrdem = True # Variável sentinela
i = 0

# Enquanto os números estiverem em ordem crescente e i for menor que N
while ((emOrdem) and (i < N)): 
    valor = int(input("Digite um número inteiro: ")) # Recebe valor

    if i == 0: # O primeiro valor vai ser o anterior
        anterior = valor
    elif valor < anterior: # Se o valor atual for menor do que o anterior é que não estão em ordem crescente
        print("Os números não estão em ordem crescente.")
        emOrdem = False

    anterior = valor # O valor atual vai virar o próximo anterior
    i += 1 # Incremento

if emOrdem:
    print("Os números estão em ordem crescente.")