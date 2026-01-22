# Desempacotamento

x, y, *resto = 1, 2, 3, 4
# x = 1
# y = 2
# resto = [3, 4]
print(x, y, resto)

def soma(*args):
    soma = 0
    for n in args:
        soma += n
    return soma
print(soma(1, 2, 3, 4, 5))