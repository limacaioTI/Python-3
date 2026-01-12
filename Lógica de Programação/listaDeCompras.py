import os

condicao = True
listaCompras = []

while condicao:
    # os.system('cls' if os.name == 'nt' else 'clear')
    print("\n=== Lista de Compras ===")
    print('Selecione uma opção:')
    opcao = input('[i]nserir, [a]pagar, [l]istar, [a]pagar: ' ).strip().lower()

    if opcao == 'i':
        listaCompras.append(input('Digite o nome do item: '))
    elif opcao == 'l':
        print("\n=== Sua lista de Compras ===")
        for indice, item in enumerate(listaCompras):
            print(f'{indice} - {item}')
    elif opcao == 'a':
        indiceRemover = int(input('Digite o índice do item que deseja remover: '))
        if 0 <= indiceRemover < len(listaCompras):
            listaCompras.pop(indiceRemover)
        else:
            print("Índice inválido.")
    elif opcao == 's':
        condicao = False
    else:
        print("Opção inválida. Tente novamente.")
        continue