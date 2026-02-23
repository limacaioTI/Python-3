# Exercício - Lista de tarefas com desfazer e refazer
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']


# def lista_dinamica(item, lista=None):
#     if lista is None:
#         lista = []
#     lista.append(item)
#     return lista


# import os

# def limpar_terminal():
#     os.system('cls' if os.name == 'nt' else 'clear')

# lista_dinamica = []
# lista_desfeitos = []

# condicao = True

# while condicao:
#     print("COMANDOS:")
#     print("1 - Adicionar")
#     print("2 - Listar")
#     print("3 - Desfazer")
#     print("4 - Refazer")
#     print("5 - Sair")
#     opcao = input('Escolha a opção: ').strip().lower()
    
#     limpar_terminal()
    
#     if opcao == '1':
#          item = input('Informe o que deseja adicionar: ')
#          lista_dinamica.append(item)   
    
#     elif opcao == '2':
#         if not lista_dinamica:
#             print("Nenhuma tarefa na lista")
            
#         else:
#             print("====== LISTA ======")
#             for posicao, elemento in enumerate(lista_dinamica):
#                 print(f"{posicao+1} - {elemento}")
#             print("===================")
        
#     elif opcao == '3':
#         if not lista_dinamica:               
#             print('A lista não possui tarefas para serem desfeitas')
#         else:
#             tarefa = lista_dinamica.pop()
#             lista_desfeitos.append(tarefa)
#     elif opcao == '4':
#         if not lista_desfeitos:
#             print('Nada para refazer')
#         else:
#             tarefa = lista_desfeitos.pop()
#             lista_dinamica.append(tarefa)
#     elif opcao == '5':
#         condicao = False
#     else:
#         print('Essa opção não é válida! ')
#         continue

# Solução mais limpa

import json
import os


def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()
    listar(tarefas)


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)


def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(tarefas, caminho_arquivo)
    return dados


def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados


CAMINHO_ARQUIVO = 'exercicio_lista_dinamica.json'
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'clear': lambda: os.system('clear'),
        'adicionar': lambda: adicionar(tarefa, tarefas),
    }
    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
        comandos['adicionar']
    comando()
    salvar(tarefas, CAMINHO_ARQUIVO)
            