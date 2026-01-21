
def valorPadrao(a, b, c):
    return a + b + c

print(valorPadrao(1, 2, 3))

def novoValorPadrao(a, b, c='Padrao'):
    return f'{a}, {b}, {c}'
print(novoValorPadrao('Valor1', 'Valor2'))

def outroValorPadrao(a, b, c):
    return f'{a}, {b}, {c}'
print(outroValorPadrao(b=2, a=7, c='C'))