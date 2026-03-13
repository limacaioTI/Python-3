num_list = [1,2,3,3,4,5,6,7,8]
unique = []

for num in num_list:
    if num not in unique:
        unique.append(num)
print(f"Unique list: {unique}")