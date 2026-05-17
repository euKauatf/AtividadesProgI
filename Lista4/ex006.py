'''6) Escreva um programa que:
(a) O funcionário fornecerá o número de candidatos N, o nome e as 3 notas de cada candidato. O programa deve armazenar os nomes dos candidatos em uma lista e a média das notas em outra lista (dado as 3 notas).
(b) Apresentar um relatório apresentando o nome dos candidatos em ordem crescente de classificação de acordo com a média obtida, como exemplo abaixo. Para isso as listas devem ser ordenadas ao mesmo tempo (por algum método).'''

# Cria as listas para armazenar os nomes e médias
#
# Recebe o número de candidatos
# Para cada i de 1 a N
#   Recebe o nome do candidato
#   Para cada j de 1 a 3
#       Recebe a nota do candidato e adiciona à lista de notas
#   Calcula a média das notas do candidato e adiciona à lista de médias
#
# Ordena as listas de nomes e médias simultaneamente
#
# Imprime o relatório dos candidatos em ordem crescente de classificação



# Criando as listas para armazenar os nomes dos candidatos e as médias das notas
nomes = []
medias = []

# Recebendo o número de candidatos
N = int(input("Digite o número de candidatos: "))

# Recebendo o nome e as 3 notas de cada candidato
for i in range(N):
    nome = input(f"Digite o nome do {i+1}º candidato: ")
    notas = []

    for j in range(3):
        nota = float(input(f"Digite a {j+1}ª nota do {nome}: "))
        notas.append(nota)
    media = sum(notas) / len(notas)

    nomes.append(nome)
    medias.append(media)

# Ordenando as listas de nomes e médias simultaneamente
candidatosOrdenados = sorted(zip(medias, nomes))

# Imprimindo o relatório dos can5didatos em ordem crescente de classificação
print("Relatório dos candidatos em ordem crescente de classificação:")
for media, nome in candidatosOrdenados:
    print(f"{nome}: Média = {media:.2f}")