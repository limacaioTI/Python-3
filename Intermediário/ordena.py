def ordena_crescente(lista, valor):
    ordena = sorted(lista, key=lambda p: p[valor])
    return ordena

def ordena_decrescente(lista, valor):
    ordena = sorted(lista, key=lambda p: p[valor], reverse=True)
    return ordena