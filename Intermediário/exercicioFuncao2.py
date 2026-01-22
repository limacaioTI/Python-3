def paridade(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

print(paridade(6))


def paridade2(numero):
    if numero % 2 == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é ímpar")

paridade2(5)