""""
Descobrir quais numeros aparecem apenas uma vez na lista
"""

nums = [1,2,3,4,4]

for i in nums:
    count = 0

    for j in nums:
        if i == j:
            count += 1

    if count == 1:
        print("Número único:", i)
        
        