# Escreva um programa que permita que o usuário indique um número de inteiros “n” a serem lidos (entre 1 e 30). Após a leitura dos “n” números, escreva na tela a média, a soma, o produto, o menor valor e o maior valor.

# soma = 0
# produto = 1
# menor = 0
# maior = 0
# Recebe N entre 1 a 30
#
# Enquanto i for menor que N
#    Recebe um numero valor
#    soma += valor
#    produto *= valor
#    Se valor > maior
#        maior = valor
#    Se valor < menor
#        menor = valor
#
# Imprime a média, soma, produto, menor e maior


# Iniciando variáveis
soma = 0
produto = 1
menor = 0
maior = 0
# Recebe N entre 1 a 30
N = int(input("Digite a quantidade de inteiros que serão inseridos (entre 1 e 30): "))

# Laço for para ler os N números
for i in range(N):
    valor = int(input("Digite um número inteiro: ")) # Recebe um numero valor
    soma += valor # soma += valor
    produto *= valor # produto *= valor

    if i == 0: # O primeiro valor vai ser o menor e maior (evita erros futuros)
        menor = valor
        maior = valor
    else:
        if valor > maior: # maior = valor caso seja maior do que o anterior
            maior = valor
        if valor < menor: # menor = valor caso seja menor do que o anterior
            menor = valor
        
media = soma / N # Calcula a média
# Imprime a média, soma, produto, menor e maior
print(f"Média: {media}")
print(f"Soma: {soma}")
print(f"Produto: {produto}")
print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")