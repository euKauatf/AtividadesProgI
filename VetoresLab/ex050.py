N = int(input("Digite um valor: "))
vetorA = [0]*N
vetorB = [0]*N
vetorC = [0]*N
vetorD = [0]*3*N
m = 0

for i in range(N):
    vetorA[i] = int(input(f"Digite um valor para a pos {i}: "))

for j in range(N):
    vetorB[j] = int(input(f"Digite um valor para a pos {j}: "))

for k in range(N):
    vetorC[k] = int(input(f"Digite um valor para a pos {k}: "))

for l in range(0, 3*N, 3):
    vetorD[l] = (vetorA[m])
    vetorD[l+1] = (vetorB[m])
    vetorD[l+2] = (vetorC[m])
    m += 1

print(vetorD)