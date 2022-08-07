# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

# SP – R$67.836,43
# RJ – R$36.678,66
# MG – R$29.229,88
# ES – R$27.165,48
# Outros – R$19.849,53

# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.


# Dados
faturamento = {}
faturamento['SP'] = 67.83643
faturamento['RJ'] = 36.67866
faturamento['RJ'] = 29.22988
faturamento['ES'] = 27.1654
faturamento['Outros'] = 19.8495

# calculando total de faturamento
def totalFaturamento(faturamento):
    totalFaturamento = 0
    for estado in faturamento:
        totalFaturamento += faturamento[estado]
        print(estado, ': ', faturamento[estado])
    return totalFaturamento

# calculando percentual de representação
def porcentagemPorEstado(faturamento, total):
    porcentagemPorEstado = {}
    for estado in faturamento:
        percentual = round((faturamento[estado] / total) * 100)
        porcentagemPorEstado[estado] = percentual

    return porcentagemPorEstado

total = totalFaturamento(faturamento)
print(f'Total: {total}')

porEstado = porcentagemPorEstado(faturamento, total)
print(f'Porcentagem por estado: {porEstado}')
