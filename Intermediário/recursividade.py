# Fatorial --> n! = 5! --> 5x4x3x2x1

# fatorial = 6
# valor = fatorial

# for i in range(1, fatorial):
#     valor = valor * i
#     i = i+1
#     print(valor)
# print(f'Fatorial de {fatorial}: {valor}')

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)
print(factorial(5))