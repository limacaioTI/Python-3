""""
Dada uma lista de números, encontre o maior número da lista.
Entrada:
nums = [3, 7, 2, 9, 4]
Saída:
9

Dica: maior é o primeiro e vai comparando

"""

nums = [1, 4, 3, 8, 33, 17, 87, 3, 67, 9, 4, 88, 110, 45]
maior_num = nums[0]

for num in nums:
    if num > maior_num:
        maior_num = num
        
print(f"Maior num: {maior_num}")