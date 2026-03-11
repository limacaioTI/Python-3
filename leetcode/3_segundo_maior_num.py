""""
Encontrar o segundo maior número
nums = [4, 7, 1, 9, 3, 9]

Saída: 7

"""
nums = [-10, -20, -5, -30]

maior = float('-inf')
segundo = float('-inf')
terceiro = float('-inf')

for num in nums:
    if num > maior:
        terceiro = segundo
        segundo = maior
        maior = num
    elif num > segundo and num != maior:
        terceiro = segundo
        segundo = num
    elif num > terceiro and num != segundo and num != maior:
        terceiro = num

print(maior, segundo, terceiro)