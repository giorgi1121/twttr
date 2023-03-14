#create variable with input
text = input().strip()

#vowels list
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

#itteration checks whether the letters in text are vowels 
#and if not prints them
for char in text:
    if char not in vowels:
        print(char, end="")
