
from ordena import ordena_crescente, ordena_decrescente

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

aumento_preco = [
    {**produto, 'preco': round(produto['preco'] * 1.1, 2) } # Duas casas decimais
    for produto in produtos
]

if __name__ == "__main__":
    
    nome_decrescente = ordena_decrescente(aumento_preco, 'nome')
    valor_crescente = ordena_crescente(aumento_preco, 'preco')
    print('Ordenando nome pelo import')
    print(*nome_decrescente, sep='\n')
    print("="*50)
    print('Ordenando preço pelo import')
    print(*valor_crescente, sep='\n')

