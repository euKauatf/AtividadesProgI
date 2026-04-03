# Exercício 3c: Em uma loja e CD's existem apenas quatro tipos de preços que estão associados a cores. Assim os CD ́s que ficam na loja não são marcados por preços e sim por cores. Desenvolva o algoritmo que a partir a entrada da cor o software mostre o preço. A loja está atualmente com a seguinte tabela de preços.
# i.    Cor         Preço
# ii.   Verde       R$ 10,00
# iii.  Azul        R$ 20,00
# iv.   Amarelo     R$ 30,00
# v.    Vermelho    R$ 40,00
#
# Recebe a cor do CD
# Analisa qual é a cor e imprime o preço correspondente

cor = input("Digite a cor do CD (verde, azul, amarelo, vermelho): ") # Recebe a cor do CD

# Sequência de condições para determinar o preço com base na cor
if (cor == "verde"):
    print("O preço do CD é R$ 10,00")
elif (cor == "azul"):
    print("O preço do CD é R$ 20,00")
elif (cor == "amarelo"):
    print("O preço do CD é R$ 30,00")
elif (cor == "vermelho"):
    print("O preço do CD é R$ 40,00")