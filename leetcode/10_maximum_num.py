num_list = [1,2,3,4,5,6, 5, 3, 9, 10, 4, 8]
maior = num_list[0]

for num in num_list:
    if num > maior:
        maior = num
print(maior)