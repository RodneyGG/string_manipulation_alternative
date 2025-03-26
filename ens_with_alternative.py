"""
Prog05. endswith() check if the string end part matches the function parameter. 
Create a program that do the same functionality without using endswith() function.
"""

#ask the user to input a word
word = input("Enter Word: ")
ending_word = input("Enter the ending word: ")
#identify if the word end with the chosen word
ends_with = True
if word[-len(ending_word):] == ending_word:
    ends_with = True
else:
    ends_with = False
#print true or false
print(ends_with)