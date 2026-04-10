# Escreva um programa para gerar dois valores aleatórios inteiros “x” e “y” entre 1 e 100, que representam o poder e a resistência de uma carta de Magic (para gerar o número aleatório usar randint). Após isso, deve-se gerar a seguinte mensagem: “quanto é o poder x multiplicado pela resistencia y da carta ?”, substituindo os números gerados por “x” e “y”. Depois da mensagem, deve ser lida uma resposta do teclado e deve ser exibido uma mensagem indicando acerto ou erro. O programa deve implementar um laço que obrigue o jogador a acertar pelo menos três vezes a resposta antes de sair. Ao final devem ser indicados o número de tentativas, de acertos e de erros.

# Importar random
# acertos = 0, erros = 0, resposta = 0
#
# Enquanto (acertos != 3):
#   x = random.randint(0, 100)
#   y = random.randint(0, 100)
#    
#   Enquanto (resposta != (x*y)):
#       recebe a resposta
#
#       Se (resposta != (x*y))
#           erros += 1
#   
#   acertos += 1
#
# imprime a qtd de tentativas, acertos e erros

#instanciando variáveis
import random

acertos = 0
erros = 0
resposta = 0

# Laço de repetição para os 3 acertos
while (acertos != 3):
        # Valores aleatórios de poder e resistência
        x = random.randint(0, 100)
        y = random.randint(0, 100)

        # Laço de repetição while até acertar
        while (resposta != (x*y)):
            resposta = int(input(f"quanto é o poder {x} multiplicado pela resistencia {y} da carta ?\n"))

            if (resposta != (x*y)): # Caso a resposta seja a errada
                print("Resposta errada. Tente novamente abaixo")
                erros += 1
        
        # Incrementa automaticamente porque saiu do while para acertar
        acertos +=1

print(f"Você finalizou o jogo em {acertos+erros} tentativas, com {acertos} acertos e {erros} erros!")