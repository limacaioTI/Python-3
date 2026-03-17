letter = "asa"
letter_palindromo = ""

for char in range(len(letter)-1, -1,-1):
    print(letter[char])
    letter_palindromo+=letter[char]

if letter == letter_palindromo:
    print(True)
else:
    print(False)

#if letter == letter[::-1]:
#    print(True)