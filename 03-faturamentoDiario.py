# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json

with open('dados.json', encoding='utf-8') as json_file:
    dados = json.load(json_file)

# verificando menor valor

def menorValor(dados):
    for dia in dados:
        if 'menorValor' in locals():
            if dia['valor'] < menorValor and dia['valor'] > 0:
                menorValor = dia['valor']
        else:
            if dia['valor'] > 0:
                menorValor = dia['valor']

    return menorValor

print('Menor valor: ', menorValor(dados))

# verificando o maior valor
def maiorValor(dados):
    for dia in dados:
        if 'maiorValor' in locals():
            if dia['valor'] > maiorValor:
                maiorValor = dia['valor']
        else:
            maiorValor = dia['valor']

    return maiorValor

print('Maior valor: ', maiorValor(dados))

# calcular média mensal
def media(dados):
    media = 0.0
    totalDias = 0
    for dia in dados:
        if dia['valor'] > 0:
            media += dia['valor']
            totalDias += 1
    return media / totalDias

print('Média mensal: ', media(dados))

# verificando o numero de dias com valor superior a média
def diasSuperiorMedia(dados):
    diasSuperiorMedia = 0
    mediaValor = media(dados)
    for dia in dados:
        if dia['valor'] > mediaValor:
            diasSuperiorMedia += 1
        # else: 
        #     print('Dia: ', dia['dia'], 'Valor: ', dia['valor'])
    return diasSuperiorMedia
    
print('Dias com valor superior a média: ', diasSuperiorMedia(dados))



