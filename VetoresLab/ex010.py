matriculasProg1 = [0]*5
matriculasProg2 = [0]*7
matriculasProg3 = [0]*7
total = 0

print("PROG1")
for i in range(len(matriculasProg1)):
    matriculasProg1[i] = int(input(f"{i+1}) "))

print("PROG2")
for j in range(len(matriculasProg2)):
    matriculasProg2[j] = int(input(f"{j+1}) "))

print("PROG3")
for k in range(len(matriculasProg3)):
    matriculasProg3[k] = int(input(f"{k+1}) "))

for l in range(len(matriculasProg1)):
    for m in range(len(matriculasProg2)):
        if matriculasProg1[l] == matriculasProg2[m]:
            for n in range(len(matriculasProg3)):
                if matriculasProg2[m] == matriculasProg3[n]:
                    print(f"Aluno {matriculasProg1[l]} irregular")
                    total+=1

print(f"total = {total}")