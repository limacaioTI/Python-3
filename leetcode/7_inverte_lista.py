""""
Exercicio para inverter lista sem usar reverse() e [::-1]
"""

num_list = [17,24,30,48,52]
num_list_reverse = []

for i in range(len(num_list)-1, 0, -1):
    num_list_reverse.append(num_list[i])

print(f"List: {num_list}")
print(f"Reverse list: {num_list_reverse}")