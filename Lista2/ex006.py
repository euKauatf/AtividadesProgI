# Calcule a soma da série S de Saitama, dado valores inteiros n e m fornecidos pelo usuário. No fim, pergunte se o usuário quer repetir a aoperação.

# continuar = 1
# Enquanto (continuar)
#   Recebe N e M
#   Sm = 0
#   Sn = 0
#   i = 1
#   j = 1
#   Enquanto i for <= N
#       Enquanto j for <= M
#           Sm += ((i**2) * j) / ((3**i) * ((j * (3**i)) + (i * (3**j))))
#           j++
#
#       Sn += Sm
#       i++
#       j = 1
#
#   Imprime Sn
#   Recebe continuar como 0 para parar e 1 para voltar do começo

# Variável sentinela para continuar
continuar = 1
while (continuar):
    # Instanciando variáveis
    N = int(input("Digite o valor N para ser somado na série S de Saitama:\n"))
    M = int(input("Digite o valor M para ser somado na série S de Saitama:\n"))
    Sm = 0
    Sn = 0
    i = 1
    j = 1

    while (i <= N): # Enquanto o somatório não chegar em N
        while (j <= M): # Enquanto o segundo somatório não cehgar em M
            Sm += ((i**2) * j) / ((3**i) * ((j * (3**i)) + (i * (3**j))))
            j+= 1
        Sn += Sm
        i+= 1
        j = 1 # Reinicia o segundo somatório
    
    print(f"O número solicitado da série S de Saitama é {Sn}!")
    
    continuar = int(input("\nDeseja executar o programa outra vez?\n1 para sim, 0 para não\n"))