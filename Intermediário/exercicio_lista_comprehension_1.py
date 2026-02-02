
estoque = [
    {
        'Produto': ['Arroz', 'Carne', 'Feijao', 'Coca-Cola'],
        'Valores': [5.50, 23.99, 7.15, 11]
    }
]

for item in estoque:
    print(item)

    for indice, produto in enumerate(item['Produto']):
        valor = item['Valores'][indice]
        print(f'{indice+1}: {produto}: R$ {valor}')

        

atualizando_valor_estoque = [
    {
        'Produto': item['Produto'],
        'Valores': [
            valor * 1.05 if valor > 10 else valor
            for valor in item['Valores']
        ]
    }
    for item in estoque
]
# print(atualizando_valor_estoque)

for item in atualizando_valor_estoque:
    print(item)
    for indice, produto in enumerate(item['Produto']):
        valor = item['Valores'][indice]
        print(f'{indice+1}: {produto}: R$ {valor}')