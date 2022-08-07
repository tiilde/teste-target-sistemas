# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

def inverterCaracter(palavra):
    palavraInvertida = ''
    for letra in range(len(palavra)):
        palavraInvertida = palavra[letra] + palavraInvertida
    return palavraInvertida

inverterCaracter(input('Digite uma palavra: '))
