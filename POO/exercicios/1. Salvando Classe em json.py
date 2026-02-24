import json

class Clube:
    def __init__(self, nome, estado):
        self.nome = nome
        self.estado = estado

# 1. Criando as instâncias
flamengo = Clube('Flamengo', 'RJ')
vasco = Clube('Vasco', 'RJ')
santos = Clube('Santos', 'SP')

# 2. Criando a lista de dicionários (o que o JSON entende)
# Usamos uma list comprehension para pegar o vars() de cada objeto
lista_clubes = [vars(flamengo), vars(vasco), vars(santos)]

CAMINHO_ARQUIVO = 'clubes.json'

def salvar(dados, caminho):
    with open(caminho, 'w', encoding='utf8') as arquivo:
        # dump: joga o dicionário para dentro do arquivo
        json.dump(dados, arquivo, indent=2, ensure_ascii=False)
    print(f"Dados salvos em {caminho}")

def ler(caminho):
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            # load: transforma o conteúdo do arquivo em objeto Python (lista/dict)
            return json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe. Criando novo arquivo...')
        salvar(lista_clubes, caminho)
        return lista_clubes

# Execução
dados_carregados = ler(CAMINHO_ARQUIVO)
print("\nDados carregados do JSON:")
print(dados_carregados)