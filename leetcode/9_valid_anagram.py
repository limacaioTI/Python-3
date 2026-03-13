""""
We need to see if in two differents words exists the same letter and length 
"""

text_1 = 'banana'
text_2 = 'banana'

list_text_1 = []
list_text_2 = []

for char in text_1:
    list_text_1.append(char)
for char in text_2:
    list_text_2.append(char)
print(list_text_1, list_text_2)

count = 0

if len(list_text_1) != len(list_text_2):
    print(False)
else:
    for i in list_text_1:
        for k in list_text_2:
            if i == k:
                count+=1
                list_text_2.remove(k)
                break
    if count == len(list_text_1):
        print(True)    
    else:
        print(False)