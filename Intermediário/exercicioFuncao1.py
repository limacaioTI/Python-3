def multiplica(*args):
    multiplicacao = 1
    for i in args:
        multiplicacao*=i
    return multiplicacao

print(multiplica(1, 2, 3, 4, 5))