'''7) Faça um programa que simule uma agenda telefônica onde o usuário informe os telefones (inteiros) e você deverá inserir estes valores de forma ordenada uma lista. O usuário deve ser capaz de inserir até 100 telefones. A cada número inserido, imprima a agenda.'''

# Cria uma lista para armazenar os telefones
#
# Para cada i de 1 a 100
#   Recebe um telefone do usuário
#   Adiciona o telefone à lista
#   Ordena a lista de telefones
#   Imprime a agenda telefônica



# Criando uma lista para armazenar os telefones
telefones = []

# Recebendo os telefones do usuário
for i in range(100):
    telefone = int(input(f"Digite o {i+1}º telefone (ou -1 para parar): "))

    if telefone == -1:
        break

    telefones.append(telefone)
    telefones.sort()
    
    print("Agenda telefônica:", telefones)