"""
Verificar a existencia de valores duplicados na lista
"""

list_ = [1, 2, 3, 4, 5, 6, 7, 2, 5, 10]
count=0

for i in range(len(list_)):
    for j in range (i+1, len(list_)):
        if list_[i] == list_[j]:
            print(f"[{list_[i]}] - [{list_[j]}]")
            count+=1

print(f"Duplicates: {count}")


# Using set

list_2 = [1, 4, 6, 7, 3, 8, 10, 4, 5, 7, 1, 7]
set_list = set()
count_num = 0

for value in list_2:
    
    if value in set_list:
        print(f"Duplicate value: {value}")
        count_num +=1
        
    set_list.add(value)
    