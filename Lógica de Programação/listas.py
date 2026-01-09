lista = []

# Adiciona elementos à lista
lista.append('maçã')
lista.append('banana')
lista.append('laranja')
print(lista)

# Remove o último elemento da lista
lista.pop()
print(lista)

# Remove o elemento 'banana' da lista
lista.remove('banana')
print(lista)

lista2 = [1, 2, 3, 4, 5]
del lista2[1]  # Remove o elemento no índice 1
print(lista2)

lista2.insert(1, 10)  # Insere o valor 10 no índice 1
print(lista2)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b  # Concatena as listas
lista_a.extend(lista_b)  # Extende lista_a com os elementos de lista_b
print(lista_a)