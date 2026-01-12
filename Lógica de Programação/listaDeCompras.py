import os

condicao = True
listaCompras = []

while condicao:
    print("\n=== Lista de Compras ===")
    print('Selecione uma opção:')
    opcao = input('[i]nserir, [a]pagar, [l]istar, [a]pagar: ' ).strip().lower()

    if opcao == 'i':
        os.system('cls')
        listaCompras.append(input('Digite o nome do item: '))
    elif opcao == 'l':
        os.system('cls')
        print("\n=== Sua lista de Compras ===")
        for indice, item in enumerate(listaCompras):
            print(f'{indice} - {item}')
    elif opcao == 'a':
        os.system('cls')
        indiceRemover = input('Digite o índice do item que deseja remover: ')
        try:
            indiceRemover = int(indiceRemover)
            if 0 <= indiceRemover < len(listaCompras):
                listaCompras.pop(indiceRemover)
            else:
                print('Digite um índice válido.')
        except IndexError:
            os.system('cls')
            print("Índice inválido.")
        except ValueError:
            os.system('cls')
            print("Por favor, insira um número válido.")

    elif opcao == 's':
        condicao = False
    else:
        os.system('cls')
        print("Opção inválida. Tente novamente.")
        continue