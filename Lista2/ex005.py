# Faca um programa que imprima os N (inteiro fornecido pelo usuário) primeiros números da série do Kirito A série inicia com os números 2,2, 3 e 3, e cada número posterior equivale a diferença entre a soma dos 2 números anteriores multiplicado por 2, e a multiplicação dos 2 números antes destes anteriores (ex: o próximo número da série eh (2*(3+3))-(2*2)=8). No fim, pergunte se o usuário quer entrar com outro N e repetir o processo.

# continuar = 1
# Enquanto (continuar)
#   Recebe N
#   v1 = 2, v2 = 2, v3 = 3, v4 = 3
#   For i até N
#     Se i+1 == 1
#         imprime v1
#     Se i+1 == 2
#         imprime v2
#     Se i+1 == 3
#         imprime v3
#     Se i+1 == 4
#         imprime v4
#     Senão
#         prox = (2 * (v4 + v3)) - (v1 * v2)
#         v4 = v3
#         v3 = v2       
#         v2 = v1
#         v1 = prox
#         imprime prox
#   Recebe o valor para continuar ou não o código

# Variável sentinela para continuar
continuar = 1
while (continuar):
    # Instanciando variáveis
    N = int(input("Digite o número de elementos da série do Kirito que deseja exibir:\n"))
    v1 = 2
    v2 = 2
    v3 = 3
    v4 = 3

    # loop for para ir exibindo os números da série
    for i in range(N):
        if (i+1 == 1):
            print(f"\n{v1}")
        elif (i+1 == 2):
            print(v2)
        elif (i+1 == 3):
            print(v3)
        elif (i+1 == 4):
            print(v4)
        else: # Quando o N for maior do que os padrões
            prox = ( (2 * (v4 + v3)) - (v1 * v2) ) # O valor a ser exibido seguirá essa fórmula
            v4 = v3 # Todos os outros irão ser rebaixados
            v3 = v2
            v2 = v1
            v1 = prox # O v1 vai ser o novo valor que foi exibido anteriormente
            print(prox)
    
    continuar = int(input("\nDeseja executar o programa outra vez?\n1 para sim, 0 para não\n"))