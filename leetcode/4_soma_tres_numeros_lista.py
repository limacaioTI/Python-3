num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 9

for i in range(len(num_list)):
    for j in range(i+1, len(num_list)):
        if num_list[i] + num_list[j] == target:
            print(f"[{i}] [{j}] -> [{num_list[i]}] + [{num_list[j]}] == {target}")

# Para a soma de 3 numeros

for i in range(len(num_list)):
    for j in range(i+1, len(num_list)):
        for k in range(j+1, len(num_list)):
            if num_list[i] + num_list[j] + num_list[k] == target:
                print(f"[{i}] [{j}] [{k}] -> [{num_list[i]}] + [{num_list[j]}] + [{num_list[k]}] == {target}")


