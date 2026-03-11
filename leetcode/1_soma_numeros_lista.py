""""
nums = [2,7,11,15]
target = 9

[0,1]

2 + 7 = 9
"""
""""
nums = [2,1,5,6,8,7,11,15]
target = 9

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])
"""

nums = [2,1,5,6,8,7,11,15]
target = 9

mapa = {}

for i, num in enumerate(nums):
    complemento = target - num
    
    if complemento in mapa:
        print([mapa[complemento], i])
    
    mapa[num] = i
