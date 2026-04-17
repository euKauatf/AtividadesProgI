N = int(input("Digite um valor: "))
vetorA = []
vetorB = []
vetorC = []
vetorD = []

for i in range(N):
    vetorA.append(int(input(f"Digite um valor para a pos {i}: ")))

for j in range(N):
    vetorB.append(int(input(f"Digite um valor para a pos {j}: ")))

for k in range(N):
    vetorC.append(int(input(f"Digite um valor para a pos {k}: ")))

for l in range(N):
    vetorD.append(vetorA[l])
    vetorD.append(vetorB[l])
    vetorD.append(vetorC[l])

print(vetorD)