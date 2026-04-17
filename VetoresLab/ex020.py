vet = [0]*5
pos = []
semrep = []

for i in range(len(vet)):
    vet[i] = int(input(f"{i+1}) "))
    if (vet[i] > 0):
        pos.append(vet[i])

for j in range(len(pos)):
    rep = False
    for k in range(len(semrep)):
        if (pos[j] == semrep[k]):
            rep = True
    if (not rep):
        semrep.append(pos[j])

print(f"vet = {vet}\npos = {pos}\nsemrep = {semrep}")