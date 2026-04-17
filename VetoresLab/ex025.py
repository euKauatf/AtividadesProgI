N = int(input("Digite um valor: "))
vetorA = []
vetorB = []
vetorC = []

for i in range(N):
    vetorA.append(int(input(f"Digite um valor para a pos {i}: ")))

for j in range(N):
    vetorB.append(vetorA[N-j-1])

for k in range(N):
    soma = 0
    for l in range(1, vetorB[k]+1):
        soma+= l
    vetorC.append(soma)

print(vetorA)
print(vetorB)
print(vetorC)

